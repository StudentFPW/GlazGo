# GlazGo
ATS (Applicant Tracking System — дословно: «система отслеживания кандидатов»)

## Внимание уважаемые коллеги !!!

```bash
Прежде чем делать commit:
    1. Пожалуйста проверьте что ваш код красивый и чистый.
    2. Токены, секретные ключи используйте через переменные окружения.
    3. Пожалуйста в файле requirements.txt сохраняйте чистоту (если вы добавляете библиотеку, добавьте только имя библиотеки, а не весь стек библиотеки).
    4. Пожалуйста, оставьте комментарий к вашему коду.
    5. Пожалуйста не добавляйте файлы виртуального окружения (Используйте gitignore https://www.toptal.com/developers/gitignore).
```

### Задача №1 Всплывающее оповещение о новом кандидате, с возможностью просмотра резюме и комментариев Рекрутера

Сигнал отслеживает сохранение изменений в таблице CandidatePromotion, в которой содержатся ссылка на сущность кандидата, сущность вакансии и продвижение кандидата по вакансии (поля Статус, дата измменения статуса)

`@receiver(post_save, sender = CandidatePromotion) 
def post_save_candidate_promotion(**kwargs):  
    instance = kwargs['instance']  
    if instance.status_change == 1: # 1 соответствует статусу Новый в списке CANDIDATE_STATUS
        Message.objects.create(user_id=instance.vacancy_id.customer, candidate_id=instance.candidat_id, viewed=False)`

Если в сохраненном экземпляре статус "Новый", то формируем данные по отправке уведомления заказчику. Данные помещаются в таблицу Message, содержащую поля: ссылка на кандидата; ссылка на заказчика (адресат сообщения); Прочитано сообщение или нет

`class Message(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.PROTECT) #ссылка на сотрудника, получатель сообщения
    candidate_id = models.ForeignKey(Candidate, on_delete=models.PROTECT) #ссылка на кандидата
    viewed = models.BooleanField('Просмотрено', default=False) #новость просмотрена`
