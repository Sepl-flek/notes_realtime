import json

from channels.generic.websocket import AsyncWebsocketConsumer


class NoteConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("notes", self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard("notes", self.channel_name)

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            "notes", {
                "type": "note_message",
                "message": data.get("message", "")
            }
        )

    async def note_message(self, event):
        await self.send(text_data=json.dumps({
            "message": event["message"]
            }))
