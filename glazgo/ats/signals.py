from datetime import datetime
from dotenv import load_dotenv
from django.db.models.signals import post_save
from django.dispatch import receiver
import os, pywhatkit
from .models import Message, CandidatePromotion, CPHistory, CallCandidate

load_dotenv()

@receiver(post_save, sender=CandidatePromotion)
def post_save_candidate_promotion(instance, **kwargs):
    # 1 соответствует статусу Новый в списке CANDIDATE_STATUS
    if instance.status_change == 1:
        Message.objects.create(
            user_id=instance.vacancy_id.customer,
            candidate_id=instance.candidat_id,
            viewed=False,
        )
    CPHistory.objects.create(
        candidat_id=instance.candidat_id,
        vacancy_id=instance.vacancy_id,
        recruter_id=instance.vacancy_id.recruter,
        status=instance.status_change,
        datetime=datetime.now(),
    )
    
    
@receiver(post_save, sender=CallCandidate)
def post_save_send_messange(**kwargs):
    instance = kwargs["instance"]
    if instance.result == False:
        recipient = instance.candidat_id
        sender = instance.candidat_id.user_id
        text = (f'Добрый день, {recipient.name} {recipient.surname}! Меня зовут {sender.name} {sender.surname}, не могу дозвониться до Вас, так как вы являетесь кандидатом на вакансию.')
        pywhatkit.sendwhatmsg_instantly(phone_no=recipient.phone, message=text)
