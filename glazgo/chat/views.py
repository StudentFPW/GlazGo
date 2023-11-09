from django.db.models import Q
from django.shortcuts import redirect, reverse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Conversation
from users.models import Users
from .serializers import ConversationListSerializer, ConversationSerializer


@api_view(["POST"])
def start_convo(request):
    """
    Функция start_convo создает разговор между двумя пользователями, если он еще не существует, и
    возвращает данные разговора.

    param request:
        Параметр request — это объект, который представляет HTTP-запрос, отправленный на
        сервер. Он содержит такую информацию, как метод запроса (например, GET, POST), заголовки и данные,
        отправленные в теле запроса
    return:
        Код возвращает объект Response. Если разговор между текущим пользователем и указанным
        участником уже существует, он перенаправляется в конечную точку «get_conversation» с идентификатором
        разговора в качестве аргумента. Если разговор не существует, он создает новый разговор между текущим
        пользователем и участником и возвращает сериализованные данные разговора.
    """
    data = request.data
    username = data.pop("username")

    try:
        participant = Users.objects.get(username=username)
    except Users.DoesNotExist:
        return Response({"message": "You cannot chat with a non existent user"})

    conversation = Conversation.objects.filter(
        Q(initiator=request.user, receiver=participant)
        | Q(initiator=participant, receiver=request.user)
    )

    if conversation.exists():
        return redirect(reverse("get_conversation", args=(conversation[0].id,)))
    else:
        conversation = Conversation.objects.create(
            initiator=request.user, receiver=participant
        )
        return Response(ConversationSerializer(instance=conversation).data)


@api_view(["GET"])
def get_conversation(request, convo_id):
    """
    Эта функция извлекает объект диалога по его идентификатору и возвращает его сериализованные данные.

    param request:
        Параметр request — это объект, который представляет HTTP-запрос, сделанный клиентом.
        Он содержит такую информацию, как метод запроса (GET, POST и т. д.), заголовки, параметры запроса и
        тело запроса
    param convo_id:
        Параметр convo_id — это идентификатор разговора, который мы хотим получить. Он
        используется для фильтрации объектов разговора и поиска разговора с соответствующим идентификатором
    return:
        Код возвращает ответ с сериализованными данными диалога, если они существуют. Если разговор
        не существует, он возвращает ответ с сообщением, указывающим, что разговор не существует.
    """
    conversation = Conversation.objects.filter(id=convo_id)

    if not conversation.exists():
        return Response({"message": "Conversation does not exist"})
    else:
        serializer = ConversationSerializer(instance=conversation[0])
        return Response(serializer.data)


@api_view(["GET"])
def conversations(request):
    """
    Эта функция извлекает список разговоров, в которых текущий пользователь является либо инициатором,
    либо получателем.

    param request:
        Параметр request — это объект, который представляет HTTP-запрос, сделанный клиентом.
        Он содержит такую информацию, как метод запроса (GET, POST и т. д.), заголовки, параметры запроса и
        пользователь, делающий запрос
    return:
        ответ, содержащий сериализованные данные списка разговоров.
    """
    conversation_list = Conversation.objects.filter(
        Q(initiator=request.user) | Q(receiver=request.user)
    )
    serializer = ConversationListSerializer(instance=conversation_list, many=True)
    return Response(serializer.data)
