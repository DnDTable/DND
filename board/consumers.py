import json
from time import time
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from datetime import datetime


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_status',
            'message': 'Выподключены с серверу'
        }))

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
