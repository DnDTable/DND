from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
import json


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = self.room_name
        self.user = User.username

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.send_to_room(_type='connection_status', message='User <b style="color: green;">' + self.user + '</b> connected', user=self.user)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def send_to_room(self, channel_name, _type='sys', message='null', user='sys', ):
        await self.channel_layer.group_send(
            channel_name | self.room_name,
            {
                'type': 'room_event',
                '_type': _type,
                'message': message,
                'user': user
            }
        )

    async def room_event(self, event):
        await self.send(text_data=json.dumps({
            'type': event['_type'],
            'message': event['message'],
            'user': event['user'],
        }))

    async def receive(self, text_data=None, bytes_data=None):
        try:
            text_data_json: dict = json.loads(text_data)

            self._type: str = text_data_json['type']
            self._message: str = text_data_json['message']
            self._user: str = text_data_json['user']
        except json.JSONDecodeError as exception:
            await self.send(text_data=json.dumps({
                'error', exception
            }))

        match self._message:
            case 'message':
                await self.send_to_room(_type=self._type, message=self._message, user=self._user)
            case 'answer':
                await self.send(text_data={self._type, self._message, self.user})
            case 'move':
                await self.send_to_room(_type=self._type, message=self._message, user=self._user)






    