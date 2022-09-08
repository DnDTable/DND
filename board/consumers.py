import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class TableConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        self.send(text_data=json.dumps({
            'type': 'connection_established',
            'message': 'You are now connected'
        }))