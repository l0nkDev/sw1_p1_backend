import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from core.models import Session

class DiagramConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["session_name"]
        self.room_group_name = f"diagram_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.accept()
        session, created = await database_sync_to_async(Session.objects.get_or_create)(id=self.room_name)
        if not created: await self.send(session.diagram)

    async def disconnect(self, close_code):
        # Called when the WebSocket closes for any reason.
        pass

    async def receive(self, text_data):
        # Called with a message received from the WebSocket.
        text_data_json: str = json.loads(text_data)
        message = text_data_json['message']
        print(json.dumps(json.loads(message)["nodes"], indent=2))
        print("\n\n\n\n\nDATA ENDS HERE\n\n\n\n\n")
        await database_sync_to_async(Session.objects.filter(id=self.room_name).update)(diagram=message)
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )
        
    async def chat_message(self, event):
        update = event["message"]
        print(f"sent data")
        await self.send(update)