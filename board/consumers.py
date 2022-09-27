from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
import json


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = 'lobby'#self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'lobby' #'chat_%s' % self.room_name
        self.user = str(User.username) 

        print('User is: ', type(self.user))
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()
        
        # await self.send_to_room('lobby', _type='connection_status', message='User <b style="color: green;">' + self.user + '</b> connected', user=self.user)

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'type': 'connection_status',
            'message': 'User <b style="color: green;">' + 'self.user' + '</b> connected',
            'user': 'User',
        }))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def send_to_room(self, channel_name='lobby', _type='sys', message='null', user='sys'):
        await self.channel_layer.group_send(
            channel_name,
            {
                'type': 'room_event',
                '_type': _type,
                'message': message,
                'user': user
            }
        )
    
    async def room_event(self, event):
        await self.send(text_data=json.dumps({
            'type': str(event['_type']),
            'message': str(event['message']),
            'user': str(event['user']),
        }))

    async def receive(self, text_data=None, bytes_data=None):
        try:
            text_data_json: dict = json.loads(text_data)

            self._type: str = text_data_json['type']
            self._message: str = text_data_json['message']
            self._user: str = text_data_json['user']

            print('type:', f"'{self._type}'", 'message:', f"'{self._message}'", 'user:', f"'{self._user}'")

            match self._type:
                case 'message':
                    await self.send_to_room(_type=self._type, message=self._message, user=self._user)
                case 'answer':
                    await self.send(text_data=json.dumps({'type': self._type, 'message': self._message, 'user': self._user}))
                case 'move':
                    await self.send_to_room(_type=self._type, message=self._message, user=self._user)

        except Exception as exception:
            await self.send(text_data=json.dumps({
                'error', exception
            }))






    