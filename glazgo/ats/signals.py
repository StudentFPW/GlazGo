from datetime import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Message, CandidatePromotion, CPHistory, Vacancy


@receiver(post_save, sender=CandidatePromotion)
def post_save_candidate_promotion(instance, **kwargs):
    """
    Приведенная функция создает сообщение и объект CPHistory, когда status_change экземпляра
    CandidatePromotion равен 1.

    param instance:
        Параметр «instance» относится к экземпляру модели CandidatePromotion, который
        вызвал сигнал post_save. Другими словами, он представляет конкретный объект, который был сохранен
        или обновлен
    """
    # 1 соответствует статусу Новый в списке CANDIDATE_STATUS
    if instance.status_change == 1:
        Message.objects.create(
            user_id=instance.vacancy_id.customer,
            candidate_id=instance.candidat_id,
            viewed=False,
        )
    else:
        CPHistory.objects.create(
            candidat_id=instance.candidat_id,
            vacancy_id=instance.vacancy_id,
            recruter_id=instance.recruter_id,
            status=instance.status_change,
            datetime=datetime.now(),  # TODO TEST THE TIME FORMAT
        )
