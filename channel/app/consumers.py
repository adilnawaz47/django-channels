from channels.consumer import SyncConsumer, AsyncConsumer
from channels.consumer import StopConsumer

class mySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('websocket connect ...', event)
        self.send({
            "type": "websocket.accept",
        })
    
    def websocket_receive(self, event):
        print('websocket received ....', event)
        print(event['text'])

    def websocket_disconnect(self, event):
        print('websocket disconnect....', event)
        raise StopConsumer()


class myAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
            print('websocket connect ...', event)
            await self.send({
                "type": "websocket.accept",
            })
    
    async def websocket_receive(self, event):
        print('websocket received ....', event)
        print(event['text'])

    async def websocket_disconnect(self, event):
        print('websocket disconnect....', event)
        raise StopConsumer()

