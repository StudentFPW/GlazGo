from django.db.models.signals import post_save
from django.dispatch import receiver
from ats.models import CandidatePromotion
from .models import Message


@receiver(post_save, sender=CandidatePromotion)
def post_save_candidate_promotion(**kwargs):
    instance = kwargs["instance"]
    # 1 соответствует статусу Новый в списке CANDIDATE_STATUS
    if instance.status_change == 1:
        Message.objects.create(
            user_id=instance.vacancy_id.customer,
            candidate_id=instance.candidat_id,
            viewed=False,
        )
