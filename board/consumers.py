from itertools import cycle
from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'room_{self.room_name}'
        self.user = 'user'
        
        self.queue = ['Laterner', 'Ksasagan'] #, 'Nectorr', 'Kotedo'
        self.pool = cycle(self.queue)
        self.current_user = next(self.pool)

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def send_to_room(self, _type='sys', message='null', user='sys'):
        await self.channel_layer.group_send(
            self.room_group_name,
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

            match self._type:
                case 'message':
                    await self.send_to_room(_type=self._type, message=self._message, user=self._user)
                case 'answer':
                    await self.send(text_data=json.dumps(
                        {'type': self._type, 'message': self._message, 'user': self._user}))
                case 'move':
                    await self.send_to_room(_type=self._type, message=self._message, user=self._user)

                    self.current_user = next(self.pool)
                    self._message = 'Ход перешёл пользователю <b style="color: yellow;">' + self.current_user + '</b>'
                    await self.send_to_room(_type='answer', message=self._message, user=self._user)  
                    await self.send_to_room(_type='currentPlayerMove', message=self.current_user, user=self._user)  
                case 'connection':
                    self.current_user = self.queue[0]
                    await self.send_to_room(_type='currentPlayerMove', message=self.current_user, user=self._user)  

                    self._message = 'Пользователь <b style="color: green;">' + self._user + '</b> присоединился'
                    await self.send_to_room(_type='connection_status', message=self._message, user=self._user)

        except Exception as exception:
            await self.send(text_data=json.dumps({
                'error', exception
            }))
