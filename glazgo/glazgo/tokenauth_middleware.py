from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
from rest_framework.authtoken.models import Token
from channels.middleware import BaseMiddleware


@database_sync_to_async
def get_user(token_key):
    """
    Функция get_user получает объект пользователя на основе заданного ключа токена или возвращает
    анонимного пользователя, если токен не существует.

    param token_key:
        Параметр token_key — это строка, представляющая ключ токена. Он используется для
        получения соответствующего объекта токена из базы данных
    return:
        Функция get_user возвращает пользователя, связанного с предоставленным ключом токена, если
        он существует в базе данных. Если токен не существует, он возвращает экземпляр AnonymousUser.
    """
    try:
        token = Token.objects.get(key=token_key)
        return token.user
    except Token.DoesNotExist:
        return AnonymousUser()


class TokenAuthMiddleware(BaseMiddleware):
    """
    Класс TokenAuthMiddleware — это промежуточное программное обеспечение, которое проверяет наличие
    токена авторизации в заголовках запроса и устанавливает атрибут user в области, если найден
    действительный токен.
    """

    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        headers = dict(scope["headers"])
        if b"authorization" in headers:
            token_name, token_key = headers[b"authorization"].decode().split()
            if token_name == "Token":
                scope["user"] = await get_user(token_key)
        return await super().__call__(scope, receive, send)
