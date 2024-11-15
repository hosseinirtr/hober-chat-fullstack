import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async  # https://pypi.org/project/asgiref/
from .models import User, Message, Room


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        username = data["username"]  # Corrected variable assignment
        this_room = data["room"]  # Corrected variable assignment

        await self.save_message(username, this_room, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "username": username,
                "room": this_room,
            },
        )

    async def chat_message(self, event):
        message = event["message"]
        username = event["username"]
        room = event["room"]

        await self.send(
            text_data=json.dumps(
                {"message": message, "username": username, "room": room}
            )
        )

    @sync_to_async
    def save_message(self, username, room, message):

        user = User.objects.get(username=username)
        room = Room.objects.get(slug=room)

        Message.objects.create(user=user, content=message, room=room)
