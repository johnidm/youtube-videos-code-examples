import logging
from typing import Any

import httpx

from config import Settings

logger = logging.getLogger(__name__)


class GupshupClient:
    def __init__(self, client: httpx.AsyncClient, settings: Settings) -> None:
        self._client = client
        self._settings = settings

    async def mark_as_read(self, message_id: str) -> None:
        url = (
            f"{self._settings.gupshup_api_base_url}/wa/app/"
            f"{self._settings.gupshup_app_id}/v3/msg"
        )
        response = await self._client.post(
            url,
            headers={
                "apikey": self._settings.gupshup_api_key,
                "Content-Type": "application/json",
            },
            json={
                "messaging_product": "whatsapp",
                "status": "read",
                "message_id": message_id,
                "typing_indicator": {"type": "text"},
            },
        )
        logger.info(
            "mark_as_read message_id=%s status=%s body=%s",
            message_id,
            response.status_code,
            response.text,
        )
        response.raise_for_status()

    async def send_text(
        self,
        destination: str,
        text: str,
        reply_to_message_id: str | None = None,
    ) -> dict:
        url = (
            f"{self._settings.gupshup_api_base_url}/wa/app/"
            f"{self._settings.gupshup_app_id}/v3/msg"
        )
        payload: dict[str, Any] = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": destination,
            "type": "text",
            "text": {"body": text},
        }
        if reply_to_message_id:
            payload["context"] = {"message_id": reply_to_message_id}

        response = await self._client.post(
            url,
            headers={
                "apikey": self._settings.gupshup_api_key,
                "Content-Type": "application/json",
            },
            json=payload,
        )
        logger.info(
            "send_text destination=%s reply_to=%s status=%s body=%s",
            destination,
            reply_to_message_id,
            response.status_code,
            response.text,
        )
        response.raise_for_status()
        return response.json()
