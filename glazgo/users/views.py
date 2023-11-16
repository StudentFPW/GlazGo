from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters

from .serializers import UserSerializer, UsersSerializer
from .models import Users


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "role",
        "phone",
    ]


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
