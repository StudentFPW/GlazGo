from django.db.models.signals import post_save
from  django.dispatch import receiver
from ats.models import CandidatePromotion

@receiver(post_save, sender = CandidatePromotion)
def post_save_candidate_promotion(**kwargs):
    print('запись создана')