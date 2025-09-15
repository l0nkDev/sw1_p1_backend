import json
from channels.generic.websocket import AsyncWebsocketConsumer

class DiagramConsumer(AsyncWebsocketConsumer):
    def connect(self):
        from .models import Session
        self.room_name = self.scope["url_route"]["kwargs"]["session_name"]
        self.room_group_name = f"diagram_{self.room_name}"
        
        self.channel_layer.group_add(
            self.room_group_name, self.channel_name
        )
        self.accept()
        s = Session.objects.get(id=self.room_name)
        print(s)
        Session.objects.get_or_create(id=self.room_name)

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