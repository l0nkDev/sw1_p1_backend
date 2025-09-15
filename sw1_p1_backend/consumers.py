import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

class DiagramConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["session_name"]
        self.room_group_name = f"diagram_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        await self.accept()
        session = await database_sync_to_async(self.get_session)(self.room_name)
        print(session.diagram)

    async def disconnect(self, close_code):
        # Called when the WebSocket closes for any reason.
        pass

    async def receive(self, text_data):
        # Called with a message received from the WebSocket.
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        print("received data")
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat.message", "message": message}
        )
        
    async def chat_message(self, event):
        update = event["message"]
        print(f"sent data")
        await self.send(update)

    def get_session(self, session_name):
        from core.models import Session
        session, created = Session.objects.get_or_create(id=session_name)
        return session