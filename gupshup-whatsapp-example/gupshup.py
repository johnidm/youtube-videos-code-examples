import json
import logging

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

    async def send_text(self, destination: str, text: str) -> dict:
        url = f"{self._settings.gupshup_api_base_url}/wa/api/v1/msg"
        message = json.dumps({"type": "text", "text": text})
        response = await self._client.post(
            url,
            headers={
                "apikey": self._settings.gupshup_api_key,
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "channel": "whatsapp",
                "source": self._settings.gupshup_source_number,
                "destination": destination,
                "src.name": self._settings.gupshup_app_name,
                "message": message,
            },
        )
        logger.info(
            "send_text destination=%s status=%s body=%s",
            destination,
            response.status_code,
            response.text,
        )
        response.raise_for_status()
        return response.json()
