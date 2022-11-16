from itertools import cycle
from channels.generic.websocket import AsyncWebsocketConsumer
import json, random


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = 'table'
        self.room_group_name = f'room_{self.room_name}'
        self.user = 'user'
        
        self.queue = ['Laterner', 'Gar', 'kotedo']
        self.pool = cycle(self.queue)

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
                    if self._message[0:3].lower() == '/d6':
                        r1 = random.randint(1, 6)
                        self._message = f"Результат броска от 1 до 6: {r1}."
                        await self.send_to_room(_type=self._type, message=self._message, user=self._user)
                    elif self._message[0:3].lower() == '/d4':
                        r1 = random.randint(1, 4)
                        self._message = f"Результат броска от 1 до 4: {r1}."
                        await self.send_to_room(_type=self._type, message=self._message, user=self._user)
                    elif self._message[0:3].lower() == '/d8':
                        r1 = random.randint(1, 8)
                        self._message = f"Результат броска от 1 до 8: {r1}."
                        await self.send_to_room(_type=self._type, message=self._message, user=self._user)
                    elif self._message[0:4].lower() == '/d10':
                        r1 = random.randint(1, 10)
                        self._message = f"Результат броска от 1 до 10: {r1}."
                        await self.send_to_room(_type=self._type, message=self._message, user=self._user)
                    elif self._message[0:4].lower() == '/d12':
                        r1 = random.randint(1, 10)
                        self._message = f"Результат броска от 1 до 12: {r1}."
                        await self.send_to_room(_type=self._type, message=self._message, user=self._user)
                    elif self._message[0:4].lower() == '/d20':
                        r1 = random.randint(1, 20)
                        r2 = random.randint(1, 20)

                        self._message = f"Результат броска от 1 до 20: {r1}."
                        await self.send_to_room(_type=self._type, message=self._message, user=self._user)
                    elif self._message[0:5].lower() == '/next':
                        self.current_user = next(self.pool)
                        self._message = 'Ход перешёл пользователю <b style="color: yellow;">' + self.current_user + '</b>'
                        await self.send_to_room(_type='answer', message=self._message, user=self._user)  
                        await self.send_to_room(_type='currentPlayerMove', message=self.current_user, user=self._user)  
                    elif self._message[0:5].lower() == '/help':
                        self._message = 'Подсказки: <br /> /help - вывод подсказок <br /> /next - передать ход<br /> ' \
                        '/d4, /d6, /d8, /d10, /d20 - бросить кубики'
                        await self.send_to_room(_type='answer', message=self._message, user=self._user)  
                    else:
                        await self.send_to_room(_type=self._type, message=self._message, user=self._user)
                    
                case 'answer':
                    await self.send(text_data=json.dumps(
                        {'type': self._type, 'message': self._message, 'user': self._user}))
                case 'move':
                    await self.send_to_room(_type=self._type, message=self._message, user=self._user)

                    # self.current_user = next(self.pool)
                    # self._message = 'Ход перешёл пользователю <b style="color: yellow;">' + self.current_user + '</b>'
                    # await self.send_to_room(_type='answer', message=self._message, user=self._user)  
                    # await self.send_to_room(_type='currentPlayerMove', message=self.current_user, user=self._user)  
                case 'connection':
                    self.current_user = self.queue[0]
                    await self.send_to_room(_type='currentPlayerMove', message=self.current_user, user=self._user)  

                    self._message = 'Пользователь <b style="color: green;">' + self._user + '</b> присоединился'
                    await self.send_to_room(_type='connection_status', message=self._message, user=self._user)

        except Exception as exception:
            await self.send(text_data=json.dumps({
                'error', exception
            }))
