from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer
from .models import Users


@api_view(["GET"])
def user_list(request):
    """
    Функция user_list извлекает список пользователей из базы данных, упорядочивает их по имени
    пользователя, сериализует данные с помощью UserSerializer и возвращает сериализованные данные в
    качестве ответа.

    param request:
        Параметр запроса — это объект, который представляет HTTP-запрос, сделанный клиентом.
        Он содержит такую информацию, как метод запроса (GET, POST и т. д.), заголовки, параметры запроса и
        тело запроса
    return:
        объект ответа, содержащий сериализованные данные всех пользователей в базе данных.
    """
    users = Users.objects.all().order_by("username")
    serializer = UserSerializer(instance=users, many=True)
    return Response(serializer.data)
