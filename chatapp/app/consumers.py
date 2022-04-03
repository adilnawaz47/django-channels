from channels.consumer import SyncConsumer,AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync


class myAsyncConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print('Websocket connected...', event)
        print('Channel Layer...', self.channel_layer ) # to get default channel layer from a project 
        print('Channel name...', self.channel_name ) # to get channel name ,
    # add channel to new existing group
        await self.channel_layer.group_add(
            'programmers', # group name
             self.channel_name
             )
        await self.send({
            'type':"websocket.accept"
        })

    async def websocket_receive(self,event):
        print('Message from client', event['text'])

        await self.channel_layer.group_send(
            'programmers',
            {
                'type': 'chat.message',
                'message': event['text']
            }
        )
    async def chat_message(self,event):
        print(' Event is  :', event)
        print(' Event is  :', type(event['message']))
        print(' Actual data  :',event['message'])

        await self.send({
                'type':"websocket.send",
                'text': event['message']
            })

    async def websocket_disconnect(self, event):
        print('Websocket is disconnected ...', event)
        await self.channel_layer.group_discard(
            'programmers',
            self.channel_name
        )
        raise StopConsumer()


class mySyncConsumer(SyncConsumer):
    def websocket_connect(self, event):
        print('Websocket connected...', event)
        print('Channel Layer...', self.channel_layer ) # to get default channel layer from a project 
        print('Channel name...', self.channel_name ) # to get channel name ,
    # add channel to new existing group
        async_to_sync(self.channel_layer.group_add)(
            'programmers', # group name
             self.channel_name
             )
        self.send({
            'type':"websocket.accept"
        })

    def websocket_receive(self,event):
        print('Message from client', event['text'])

        async_to_sync(self.channel_layer.group_send)(
            'programmers',
            {
                'type': 'chat.message',
                'message': event['text']
            }
        )
    def chat_message(self,event):
        print(' Event is  :', event)
        print(' Event is  :', type(event['message']))
        print(' Actual data  :',event['message'])

        self.send({
                'type':"websocket.send",
                'text': event['message']
            })

    def websocket_disconnect(self, event):
        print('Websocket is disconnected ...', event)
        async_to_sync(self.channel_layer.group_discard )(
            'programmers',
            self.channel_name
        )
        raise StopConsumer()