from datetime import timedelta

from django.utils.timezone import now
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, filters

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


# def get_message(user):
#     """
#     функция получения кверисета непрочтенных сообщений адресованных текущему пользователю
#     """
#     return Message.objects.filter(user_id__username=user, viewed=False)


# class MessageViewSet(viewsets.ModelViewSet):
#     serializer_class = MessageSerializer
#     queryset = Message.objects.all()
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
#     ordering_fields = "__all__"
#     filterset_fields = [
#         "user_id",
#         "candidate_id",
#         "viewed",
#     ]

#     def get_queryset(self):
#         print(f"Test: User {self.request.user}")

#         qs = get_message(self.request.user)

#         print(f"Test: Message {qs}")

#         return qs


# class WaitingCandidateViewSet(viewsets.ModelViewSet):
#     serializer_class = WaitingCandidateSerializer
#     queryset = CandidatePromotion.objects.all()
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
#     ordering_fields = "__all__"
#     filterset_fields = [
#         "candidat_id",
#         "status_change",
#     ]

#     def get_queryset(self):
#         print(f"Test: User {self.request.user}")

#         qs = CandidatePromotion.objects.filter(
#             vacancy_id__customer__username=self.request.user,
#             agreed=False,
#             status_change_date__lt=now() - timedelta(days=1),
#         )

#         print(f"Test: Message {qs}")

#         return qs
