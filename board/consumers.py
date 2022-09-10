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
            'type': 'connection_established',
            'message': 'You are now connected'
        }))

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            # if text_data_json['type'] == 'message':
            #     self.send(text_data_json['message'])
            # if text_data_json['type'] == 'answer':
            #     self.send(str({'type':'answer', 'message': str(datetime.now())}))

            message = text_data_json['message']

            # self.send(type(text_data_json))
        except:
            # self.send(str(text_data))
            message = text_data
            # self.send("str: " + text_data)
        # print('ssssssssssssssssssssssss------------------------------', text_data)

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'room_event',
                'message': message,
            }
        )

    def room_event(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type': 'message',
            'message': message
        }))
