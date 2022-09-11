import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime
import random

nick_names = [
    'Пипидастр',
    'Юсуф',
    'Маркалей',
    'Гусь',
    'Кирпич',
    'Медведь',
    'Олень',
    'Реджеп',
    'Ягода',
]


class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usernames = nick_names
        self.current_names = []

    async def connect(self):
        self.room_group_name = 'test'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
        user = self.usernames[random.randint(0, len(self.usernames) - 1)]
        # self.usernames.pop(self.usernames.index(user))

        await self.send(text_data=json.dumps({
            'type': 'connection_status',
            'message': f'Выподключены с серверу. Ваш ник - {user}',
            'user': user
        }))
        await self.send_room("Пользователь <b style='color: green;'>" + user + "</b> присоединился к чату", user)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name, self.channel_name
        )

    async def send_room(self, message, user):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'room_event',
                'message': message,
                'user': user,
            }
        )

    async def send_yourself(self, message, user):
        await self.send(text_data=json.dumps({
            'type': 'message',
            'message': message,
            'user': user
        }))

    async def receive(self, text_data):
        user = "user"
        try:
            text_data_json = json.loads(text_data)
            if text_data_json['type'] == 'message':
                message = text_data_json['message']
                user = text_data_json['user']
                await self.send_room(message, user)
            elif text_data_json['type'] == 'answer':
                message = str(datetime.now())
                user = "server timer"
                await self.send_yourself(message, user)
            else:
                pass


        except:
            message = text_data

    async def room_event(self, event):
        message = event['message']
        user = event['user']

        await self.send(text_data=json.dumps({
            'type': 'message',
            'message': message,
            'user': user
        }))
