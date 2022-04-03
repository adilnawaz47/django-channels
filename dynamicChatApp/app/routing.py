from . import consumers
from django.urls import path

websocket_urlpattterns = [
    path('ws/sc/<str:groupname>/', consumers.mySyncConsumer.as_asgi()),
    path('ws/ac/<str:groupname>/', consumers.myAsyncConsumer.as_asgi()),
]