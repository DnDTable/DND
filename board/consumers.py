import json
from mimetypes import init
from time import time
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
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

class ChatConsumer(WebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.usernames = nick_names
        self.current_names = []

    def connect(self):
        self.room_group_name = 'test'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        user = self.usernames[random.randint(0, len(self.usernames) - 1)]
        # self.usernames.pop(self.usernames.index(user))
        
        self.send(text_data=json.dumps({
            'type': 'connection_status',
            'message': f'Выподключены с серверу. Ваш ник - {user}',
            'user': user
        }))
        self.send_room("Пользователь <b style='color: green;'>" + user + "</b> присоединился к чату", user)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def send_room(self, message, user):
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'room_event',
                    'message': message,
                    'user': user,
                }
            )
    
    def send_yourself(self, message, user):
            self.send(text_data=json.dumps({
                'type': 'message',
                'message': message,
                'user': user
            }))

    def receive(self, text_data):
        user = "user"
        try:
            text_data_json = json.loads(text_data)
            if text_data_json['type'] == 'message':
                message = text_data_json['message']
                user = text_data_json['user']
                self.send_room(message, user)
            elif text_data_json['type'] == 'answer':
                message = str(datetime.now())
                user = "server timer"
                self.send_yourself(message, user)
            else:
                pass
            

        except:
            message = text_data



    def room_event(self, event):
        message = event['message']
        user = event['user']

        self.send(text_data=json.dumps({
            'type': 'message',
            'message': message,
            'user': user
        }))
