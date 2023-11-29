from rest_framework import viewsets, filters
from rest_framework_rules.mixins import PermissionRequiredMixin
from rest_framework import viewsets, filters

from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializer import *
from users.permissions import UserRecruiter


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


class CPHistoryViewSet(PermissionRequiredMixin, viewsets.ModelViewSet):
    # permission_classes = [UserRecruiter]
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
    permission_classes = [UserRecruiter]
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
