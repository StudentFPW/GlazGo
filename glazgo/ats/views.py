from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializer import *
from users.models import User as UserX


class TeamViewSet(viewsets.ModelViewSet):
    """
    Класс TeamViewSet — это набор представлений, который обрабатывает операции CRUD для модели Team с
    дополнительной логикой для фильтрации набора запросов на основе текущего пользователя и добавления
    текущего пользователя в качестве участника при создании новой команды.
    """

    serializer_class = TeamSerializer
    queryset = Team.objects.all()

    def get_queryset(self):
        return self.queryset.filter(members__in=[self.request.user]).first()

    def perform_create(self, serializer):
        obj = serializer.save(created_by=self.request.user)
        obj.members.add(self.request.user)
        obj.save()


@api_view(["GET"])
def get_my_team(request):
    """
    Эта функция извлекает команду, членом которой является текущий пользователь, и возвращает ее
    сериализованные данные.

    :param request:
        Объект запроса содержит информацию о текущем HTTP-запросе, например, о пользователе,
        делающем запрос, и любых данных, отправленных вместе с запросом

    :return:
        Ответ будет содержать сериализованные данные командного объекта.
    """
    team = Team.objects.filter(members__in=[request.user]).first()
    serializer = TeamSerializer(team)
    return Response(serializer.data)


@api_view(["POST"])
def add_member(request):  # TODO Эту функцию нужно переопределить !!!
    team = Team.objects.filter(members__in=[request.user]).first()
    username = request.data["username"]
    user = UserX.objects.get(username=username)
    team.members.add(user)
    team.save()
    return Response()


class RFOViewSet(viewsets.ModelViewSet):
    serializer_class = RFOSerializer
    queryset = ReasonForOpening.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "id",
        "text",
    ]


class WorkTimeViewSet(viewsets.ModelViewSet):
    serializer_class = WorkTimeSerializer
    queryset = WorkTime.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "id",
        "time",
    ]


class RegionViewSet(viewsets.ModelViewSet):
    serializer_class = RegionSerializer
    queryset = Region.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "id",
        "name",
    ]


class CandidateBaseViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateBaseSerializer
    queryset = CandidateBase.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "id",
        "datetime",
    ]


class CPHistoryViewSet(viewsets.ModelViewSet):
    serializer_class = CPHistorySerializer
    queryset = CPHistory.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "id",
        "candidat_id",
        "vacancy_id",
        "recruter_id",
        "status",
        "datetime",
    ]


class VacancyViewSet(viewsets.ModelViewSet):
    serializer_class = VacancySerializer
    queryset = Vacancy.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "id",
        "recruter",
        "customer",
        "status_vacancy",
        "salary",
    ]

    def perform_create(self, serializer):
        """
        Функция назначает команду и пользователя, создавшего ее, объекту сериализатора.
        """
        team = Team.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team, created_by=self.request.user)

    # def perform_update(self, serializer):
    #     """
    #     Функция «perform_update» обновляет поле назначенного объекта объекта на основе member_id, указанного
    #     в данных запроса.
    #     """
    #     obj = self.get_object()
    #     member_id = self.request.data["assigned_to"]
    #     if member_id:
    #         user = User.objects.get(pk=member_id)
    #         serializer.save(assigned_to=user)
    #     else:
    #         serializer.save()

    def get_queryset(self):
        """
        Функция возвращает отфильтрованный набор запросов на основе команды текущего пользователя.

        :return:
            Метод get_queryset возвращает отфильтрованный набор запросов. Сначала он извлекает объект
            Team, где поле Members содержит self.request.user (текущий пользователь), а затем фильтрует набор
            запросов на основе полученной команды.
        """
        team = Team.objects.filter(members__in=[self.request.user]).first()
        return self.queryset.filter(team=team)


class CandidateViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateSerializer
    queryset = Candidate.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "id",
        "email",
        "phone",
        "birthday",
    ]


class CPromotionViewSet(viewsets.ModelViewSet):
    serializer_class = CPromotionSerializer
    queryset = CandidatePromotion.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    ordering_fields = "__all__"
    filterset_fields = [
        "id",
        "candidat_id",
        "vacancy_id",
        "recruter_id",
        "status_change",
        "status_change_date",
    ]


class CandidateAddedViewSet(viewsets.ModelViewSet):
    serializer_class = CandidateAddedSerializer
    queryset = Candidate.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    http_method_names = ["post"]
    ordering_fields = "__all__"
    filterset_fields = [
        "candidat_id",
        "status_change",
    ]
