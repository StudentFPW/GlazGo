import pywhatkit
import pandas as pd

from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.response import Response
from rest_framework import status
from tablib import Dataset

from .models import *


@receiver(post_save, sender=CandidateBase)
def post_save_candidate_base(instance, **kwargs):
    file = instance.file
    df = pd.read_excel(file)

    rename_columns = {
        "Фамилия": "surname",
        "Имя": "name",
        "Емайл": "email",
        "Телефон": "phone",
        "Ресурс": "source",
        "Отчество": "otch",
        "День рождения": "birthday",
        "Транспорт": "auto",
    }
    df.rename(columns=rename_columns, inplace=True)
    candidate_resource = CandidateResource()
    dataset = Dataset().load(df)
    result = candidate_resource.import_data(dataset, dry_run=True, raise_errors=True)
    if not result.has_errors():
        result = candidate_resource.import_data(dataset, dry_run=False)
        return Response({"status": "Candidate Data Imported Successfully"})
    return Response(
        {"status": "Not Imported Candidate Data"},
        status=status.HTTP_400_BAD_REQUEST,
    )


@receiver(post_save, sender=CandidatePromotion)
def post_save_candidate_promotion(instance, **kwargs):
    if instance.status_change == 1:
        Message.objects.create(
            user_id=instance.vacancy_id.customer,
            candidate_id=instance.candidat_id,
            viewed=False,
        )
    CPHistory.objects.create(
        candidat_id=instance.candidat_id,
        vacancy_id=instance.vacancy_id,
        recruter_id=instance.recruter_id,
        status=instance.status_change,
        datetime=datetime.now(),
    )


@receiver(post_save, sender=CallCandidate)
def post_save_send_messange(instance, **kwargs):
    if instance.result == False:
        recipient = instance.candidat_id
        sender = instance.candidat_id.user_id
        text = f"Добрый день, {recipient.name} {recipient.surname}! Меня зовут {sender.name} {sender.surname}, не могу дозвониться до Вас, так как вы являетесь кандидатом на вакансию."
        pywhatkit.sendwhatmsg_instantly(phone_no=recipient.phone, message=text)
