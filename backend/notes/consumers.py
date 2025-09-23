import json
from channels.generic.websocket import AsyncWebsocketConsumer
import logging

logger = logging.getLogger(__name__)


class NoteConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info("WebSocket connect from %s", self.scope.get("client"))
        await self.accept()
        await self.send(text_data=json.dumps({"message": "connected"}))

    async def receive(self, text_data):
        logger.info("WebSocket receive: %s", text_data)
        data = json.loads(text_data)
        await self.send(text_data=json.dumps({"message": f"echo: {data}"}))

    async def disconnect(self, close_code):
        logger.info("WebSocket disconnect: %s", close_code)
