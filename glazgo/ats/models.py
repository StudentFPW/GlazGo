from django.db import models
from django.conf import settings

from import_export import resources


class CandidateBase(models.Model):
    file = models.FileField("Файл с базой кандидатов", null=False)


class CPHistory(models.Model):
    """
    Класс CPHistory представляет историю продвижения кандидата на вакансию, включая его
    статус, время его записи и любые комментарии...
    """

    candidat_id = models.ForeignKey(
        "Candidate", on_delete=models.CASCADE, related_name="CPHC"
    )
    vacancy_id = models.ForeignKey(
        "Vacancy", on_delete=models.CASCADE, related_name="CPHV"
    )
    recruter_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="CPHR"
    )

    status = models.IntegerField("Статус", default=0)
    datetime = models.DateTimeField("Зафиксированное время", auto_now_add=True)

    def __str__(self):
        return f"Дата: {self.datetime}"

class Vacancy(models.Model):
    """
    Класс Vacancy представляет вакансию с различными атрибутами, такими как дата создания, работодатель,
    рекрутер, описание должности, местоположение, диапазон заработной платы и требования.
    """

    VACANCY_STATUS = [
        (1, "Открыта"),
        (2, "Закрыта"),
        (3, "Приостановлена"),
    ]

    INTERN_TYPE = [
        (1, "Наставник"),
        (2, "Мерчендайзер"),
        (3, "Супервайзер"),
        (4, "Удаленно"),
    ]

    recruter = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="recruters"
    )
    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="customers"
    )

    # Необходимые поля
    name_vacancy = models.CharField("Название вакансии", max_length=250)
    region = models.CharField("Место работы", max_length=250)
    schedule = models.CharField("График работы", max_length=30)
    cause = models.CharField("Причина открытия вакансии", max_length=500)

    # Необязательные поля
    date_cust = models.DateTimeField("Дата поступления вакансии", auto_now_add=True)
    description_vacancy = models.TextField("Описание вакансии", null=True)
    salary = models.IntegerField("Зарплата", default=0)
    motivation = models.IntegerField("Дополнительная мотивация (Сумма)", default=0)
    auto = models.BooleanField("Наличие автомобиля", default=False)
    gsm = models.IntegerField("Расходы на топливо", default=0)
    substitute = models.BooleanField("Подменный сотрудник", default=False)
    type_job = models.BooleanField("Удаленная работа", default=False)
    intern = models.IntegerField("Вид стажировки", choices=INTERN_TYPE, default=1)
    count_hours = models.IntegerField("Среднее количество часов в день", null=True)
    count_tt = models.IntegerField("Среднее количество ТТ в день", null=True)
    status_vacancy = models.IntegerField(
        "Статус вакансии", choices=VACANCY_STATUS, default=1
    )

    def __str__(self):
        return f"ИД рекрутера: {self.recruter}, Название вакансии: {self.name_vacancy}, Заказчик:{self.customer}"


class Candidate(models.Model):
    """
    Класс «Кандидат» представляет кандидата на должность и содержит различные поля, такие как имя,
    фамилия, дата рождения, адрес электронной почты, номер телефона и т. д.
    """

    INVITED = [
        (1, "Импорт"),
        (2, "Ручной ввод"),
    ]

    # Необходимые поля
    surname = models.CharField("Фамилия", max_length=20)
    name = models.CharField("Имя", max_length=20)
    email = models.EmailField("Почта")
    phone = models.CharField("Телефон", max_length=15)
    source = models.TextField("Источник")
    resume = models.FileField("Файл резюме", null=False)

    # Необязательные поля
    otch = models.CharField("Отчество", max_length=20, null=True)
    birthday = models.DateField("Дата рождения", null=True)
    referral_program = models.IntegerField(
        "Откуда кандидат", choices=INVITED, default=1
    )
    auto = models.BooleanField("Наличие автомобиля", default=False)

    def __str__(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}, Почта: {self.email}"


class CandidateResource(resources.ModelResource):
    class Meta:
        model = Candidate
        import_id_fields = ["email"]
        skip_unchanged = True
        use_bulk = True


class CandidatePromotion(models.Model):
    """
    Класс CandidatePromotion представляет продвижение кандидата на конкретную вакансию, включая такую
    информацию, как идентификаторы кандидата и вакансии, изменение статуса, дата изменения статуса, дата
    назначения, статус события и комментарий.
    """

    CANDIDATE_STATUS = [
        (1, "Новый"),
        (2, "Созвон"),
        (3, "3-й недозвон"),
        (4, "Резюме"),
        (5, "Стажировка"),
        (6, "Оформление"),
        (7, "Отказ"),
        (8, "Кадровый резерв"),
    ]

    candidat_id = models.ForeignKey(
        Candidate, on_delete=models.PROTECT, related_name="candidat"
    )
    vacancy_id = models.ForeignKey(
        Vacancy, on_delete=models.PROTECT, related_name="vacancy"
    )
    recruter_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="recruter"
    )
    status_change = models.IntegerField(
        "Текущий статус", choices=CANDIDATE_STATUS, default=1
    )
    status_change_date = models.DateTimeField(
        "Дата изменения статуса", auto_now_add=True
    )

    appointment_date = models.DateField("Назначенная дата", null=True)
    event = models.BooleanField("Состоялось событие", default=False)
    comment = models.TextField("Коментарий", null=True)

    def __str__(self):
        return f"ИД кандидата: {self.candidat_id}, ИД вакансии: {self.vacancy_id}, ИД рекрутера: {self.recruter_id}, Статус: {self.status_change}, Дата: {self.status_change_date}"


class Message(models.Model):
    """
    Класс, хранящий сведения о новых кандидатах и получателях сообщения
    """

    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="user_messages"
    )
    candidate_id = models.ForeignKey(
        Candidate, on_delete=models.PROTECT, related_name="candidate_messages"
    )

    viewed = models.BooleanField("Просмотрено", default=False)

    def __str__(self):
        return f"ИД пользователи: {self.user_id}, ИД кандидата: {self.candidate_id}, Просмотрено: {self.viewed}"


class CallCandidate(models.Model):
    """
    Класс, хранящий сведения о результатах созвона с кандидатом
    """

    candidate_id = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    vacancy_id = models.ForeignKey(Vacancy, on_delete=models.CASCADE)
    result = models.BooleanField("Разговор состоялся", default=False)
    comment = models.CharField("Комментарий сотрудника", max_length=250, null=True)
    date_call = models.DateTimeField("Дата и время звонка", auto_now_add=True)
