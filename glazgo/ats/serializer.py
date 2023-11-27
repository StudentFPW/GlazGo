from rest_framework import serializers

from .models import *
from users.models import User
from users.serializers import UserDetailsSerializer
import random


class CPHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CPHistory
        fields = "__all__"


class ResponsibilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsibilities
        fields = "__all__"


class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = "__all__"


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = "__all__"


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CPromotionSerializer(serializers.ModelSerializer):
    candidat_id = CandidateSerializer()
    vacancy_id = VacancySerializer()
    recruter_id = UserSerializer()
    class Meta:
        model = CandidatePromotion
        fields = ("status_change", "status_change_date", "appointment_date", "event", "comment", "agreed", "candidat_id", "vacancy_id", "recruter_id")


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class WaitingCandidateSerializer(serializers.ModelSerializer):
    candidat = CandidateSerializer(required=False)
    vacancy = VacancySerializer(required=False)

    class Meta:
        model = CandidatePromotion
        fields = "__all__"

class CandidateAddedSerializer(serializers.ModelSerializer):
    """
    Класс CandidateAddedSerializer предназначен для сохранения нового кандидата.
    """
    surname = serializers.CharField()
    name = serializers.CharField()
    otch = serializers.CharField()
    birthday = serializers.DateField()
    phone = serializers.CharField()
    ref = serializers.CharField()
    resume = serializers.CharField()
    comment = serializers.CharField(required=False)
    vacancy = serializers.IntegerField(required=False)

    class Meta:
        model = Candidate
        fields = ('surname', 'name', 'otch', 'birthday', 'phone', 'ref', 'resume', 'comment', 'vacancy')


    def create(self, validated_data):
        # разбиваем словарь validated_data на таблицы
        comment_date = validated_data.pop('comment')
        vacancy_id = validated_data.pop('vacancy')
        # Создаем нового кандидата из оставшихся данных в validated_data
        candidate = Candidate.objects.create(**validated_data)
        # Получение объекта Vacancy по vacancy_id
        vacancy = Vacancy.objects.get(pk=vacancy_id)
        # Отбираю пользователей из User, где поле role соответствует рекрутеру и рекрутеру администратору
        recruters = User.objects.filter(role__in=[1, 2])
        # из отобранного списка рекрутеров, случайным образом выбираю одного
        recruter = recruters[random.randint(0, recruters.count()-1)]

        candidate_promotion_new = CandidatePromotion.objects.create(candidat_id=candidate, comment=comment_date,
                                                                    vacancy_id=vacancy, recruter_id=recruter)
        return candidate


