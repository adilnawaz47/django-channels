from . import consumers
from django.urls import path

websocket_urlpattterns = [
    path('ws/sc/', consumers.mySyncConsumer.as_asgi()),
    path('ws/ac/', consumers.myAsyncConsumer.as_asgi()),
]