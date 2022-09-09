import json
from time import time
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from datetime import datetime

class TableConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected'
        }))

    def receive(self, text_data):

        try:
            text_data_json = json.loads(text_data)
            if text_data_json['type'] == 'message':
                self.send(text_data_json['message'])
            if text_data_json['type'] == 'answer':
                self.send(str({'type':'answer', 'message': str(datetime.now())}))
        except:
            self.send(str(text_data))
        # print('ssssssssssssssssssssssss------------------------------', text_data)
        