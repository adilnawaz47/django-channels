from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer

class mySyncConsumer(SyncConsumer):
    def websocket_connect(self,event):
        print('The event is : ', event)
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print('The receive packet is : ', event['text'])
        self.send({
            'type': 'websocket.send',
            'text': 'Message sent to client ..??'
        })

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
        await self.send({
            'type': 'websocket.send',
            'text': 'Message sent to client ..??'
        })

    async def websocket_disconnect(self, event):
        print('websocket is disconnected ...', event)
        raise StopConsumer()
