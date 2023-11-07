from django.db import models
from datetime import datetime, date
from django.utils import timezone

from ats.models import Users, Candidate

#Класс, хранящий сведения о новых кандидатах и получателях сообщения
class Message(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT) #ссылка на сотрудника, получатель сообщения
    candidate_id = models.ForeignKey(Candidate, on_delete=models.PROTECT) #ссылка на кандидата
    viewed = models.BooleanField('Просмотрено', default=False) #новость просмотрена