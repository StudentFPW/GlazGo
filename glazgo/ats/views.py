from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializer import *
from users.models import User as UserX


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def list(self, request):
        """
        Функция возвращает список проектов, участником которых является текущий пользователь.
        """
        queryset = Project.objects.filter(members__in=[self.request.user])
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        """
        Функция «perform_create» сохраняет сериализованный объект, устанавливает в поле «create_by» текущего
        пользователя, добавляет текущего пользователя в поле «members» и сохраняет объект.
        """
        user = UserX.objects.get(pk=self.request.user.pk)
        if user.role == 1 or user.role == 2:
            obj = serializer.save(created_by=self.request.user)
            obj.members.add(self.request.user)
            obj.save()

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass


@api_view(["POST"])
def add_member(request):
    """
    Функция add_member добавляет пользователя в список участников проекта, если пользователь, сделавший
    запрос, является создателем проекта.
    """
    project = Project.objects.get(pk=request.data["pk"])
    user = UserX.objects.get(username=request.data["username"])
    if request.user.id == project.created_by.id:
        project.members.add(user)
        project.save()
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
        team = Project.objects.filter(members__in=[self.request.user]).first()
        serializer.save(team=team, created_by=self.request.user)

    def perform_update(self, serializer):
        """
        Функция «perform_update» обновляет поле назначенного объекта объекта на основе member_id, указанного
        в данных запроса.
        """
        obj = self.get_object()
        member_id = self.request.data["recruter"]
        if member_id:
            user = UserX.objects.get(pk=member_id)
            serializer.save(recruter=user)
        else:
            serializer.save()

    def get_queryset(self):
        """
        Функция возвращает отфильтрованный набор запросов на основе команды текущего пользователя.

        :return:
            Метод get_queryset возвращает отфильтрованный набор запросов. Сначала он извлекает объект
            Team, где поле Members содержит self.request.user (текущий пользователь), а затем фильтрует набор
            запросов на основе полученной команды.
        """
        team = Project.objects.filter(members__in=[self.request.user]).first()
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
