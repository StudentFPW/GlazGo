from django.urls import re_path

from . import consumers

# Этот фрагмент кода определяет шаблон URL-адреса для соединений WebSocket в приложении Django.
websocket_urlpatterns = [
    re_path(r"ws/chat/(?P<room_name>\w+)/$", consumers.ChatConsumer.as_asgi()),
]
