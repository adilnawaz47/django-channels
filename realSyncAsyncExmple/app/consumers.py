from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio

class mySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('The event is : ', event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print('The receive packet is : ', event['text'])
        for i in range(50):
            self.send({
                'type': 'websocket.send',
                'text': str(i)
            })
            sleep(1)

    def websocket_disconnect(self, event):
        print('websocket is disconnected ...', event)
        raise StopConsumer()


class myAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('The event is : ', event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print('The receive packet is : ', event['text'])
        for i in range(50):
            await self.send({
                'type': 'websocket.send',
                'text': str(i)
            })
            await asyncio.sleep(1)

    async def websocket_disconnect(self, event):
        print('websocket is disconnected ...', event)
        raise StopConsumer()
