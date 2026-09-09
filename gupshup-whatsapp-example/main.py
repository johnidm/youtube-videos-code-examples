import json
import logging
from contextlib import asynccontextmanager
from typing import Any

import httpx
from fastapi import BackgroundTasks, FastAPI, HTTPException, Request, Response
from pydantic import BaseModel, ConfigDict, ValidationError

from config import settings
from gupshup import GupshupClient

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

REPLY_TEXT = "Message received"


class InboundMessage(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: str
    source: str
    type: str


class InboundEvent(BaseModel):
    model_config = ConfigDict(extra="ignore")

    type: str
    payload: dict[str, Any] | None = None


class SendMessageRequest(BaseModel):
    destination: str
    text: str


def extract_text_messages(data: dict[str, Any]) -> list[InboundMessage]:
    """Parse inbound text messages from Gupshup v2 or Meta Cloud API payloads."""
    if data.get("object") == "whatsapp_business_account":
        messages: list[InboundMessage] = []
        for entry in data.get("entry", []):
            for change in entry.get("changes", []):
                value = change.get("value", {})
                for msg in value.get("messages", []):
                    if msg.get("type") != "text":
                        continue
                    try:
                        messages.append(
                            InboundMessage(
                                id=msg["id"],
                                source=msg["from"],
                                type=msg["type"],
                            )
                        )
                    except (KeyError, ValidationError):
                        logger.warning("Skipping malformed Cloud API message: %s", msg)
        return messages

    try:
        event = InboundEvent.model_validate(data)
    except ValidationError:
        return []

    if event.type != "message" or event.payload is None:
        return []

    try:
        message = InboundMessage.model_validate(event.payload)
    except ValidationError:
        logger.warning("Invalid Gupshup message payload: %s", event.payload)
        return []

    if message.type != "text":
        return []

    return [message]


@asynccontextmanager
async def lifespan(app: FastAPI):
    client = httpx.AsyncClient(timeout=10.0)
    app.state.gupshup = GupshupClient(client, settings)
    yield
    await client.aclose()


app = FastAPI(title="Gupshup WhatsApp Webhook", lifespan=lifespan)


@app.get("/")
def health_check():
    return {"app_name": settings.gupshup_app_name}


@app.post("/messages")
async def send_message(request: Request, payload: SendMessageRequest):
    try:
        return await request.app.state.gupshup.send_text(payload.destination, payload.text)
    except httpx.HTTPError as exc:
        logger.error("Failed to send message to %s: %s", payload.destination, exc)
        raise HTTPException(
            status_code=502,
            detail="Failed to send message via Gupshup",
        ) from exc


@app.post("/webhook")
async def webhook(request: Request, background_tasks: BackgroundTasks):
    body = await request.body()

    try:
        data = json.loads(body)
    except json.JSONDecodeError as exc:
        logger.warning("Invalid webhook JSON: %s", exc)
        return Response(status_code=200)

    messages = extract_text_messages(data)
    if not messages:
        logger.info("No text messages to process")
        return Response(status_code=200)

    for message in messages:
        background_tasks.add_task(
            handle_message,
            request.app.state.gupshup,
            message.id,
            message.source,
        )
    return Response(status_code=200)


async def handle_message(gupshup: GupshupClient, message_id: str, source: str) -> None:
    try:
        await gupshup.mark_as_read(message_id)
    except httpx.HTTPError as exc:
        logger.error("Failed to mark message as read: %s", exc)

    try:
        await gupshup.send_text(source, REPLY_TEXT)
    except httpx.HTTPError as exc:
        logger.error("Failed to send reply: %s", exc)
