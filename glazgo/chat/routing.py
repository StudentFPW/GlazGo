from django.urls import re_path

from . import consumers

# This code snippet is defining a URL pattern for WebSocket connections in a Django application.
websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]
