from rest_framework import serializers

from .models import *


class RFOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReasonForOpening
        fields = "__all__"


class WorkTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkTime
        fields = "__all__"


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = "__all__"


class CandidateBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidateBase
        fields = "__all__"


class CPHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CPHistory
        fields = "__all__"


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"


class CPromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandidatePromotion
        fields = "__all__"


# class MessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Message
#         fields = "__all__"


# class WaitingCandidateSerializer(serializers.ModelSerializer):
#     candidat = CandidateSerializer(required=False)
#     vacancy = VacancySerializer(required=False)

#     class Meta:
#         model = CandidatePromotion
#         fields = "__all__"
