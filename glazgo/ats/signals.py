from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Message, CandidatePromotion, CPHistory


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
