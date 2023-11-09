from django.db import models
from django.conf import settings


class Customer(models.Model):
    """
    Класс «Клиент» представляет клиента с различными атрибутами, такими как
    название компании, описание, адреса, ИНН, текущий счет, телефон и адрес электронной почты.
    """

    company_name = models.CharField("Название организации", max_length=30)
    description = models.TextField("Описание организации")
    legal_address = models.CharField("Юридический адрес", max_length=250)
    mailing_address = models.CharField("Почтовый адрес", max_length=250)
    inn = models.CharField("ИНН", max_length=10)
    checking_account = models.CharField("Расчетный счет", max_length=20)
    phone = models.CharField("Телефон", max_length=15)
    email = models.EmailField("Электронная почта")

    def __str__(self):
        return f"customer: {self.name_customer}"


class Responsibilities(models.Model):
    """
    Класс Responsibilities представляет собой модель хранения описаний обязанностей и управления ими.
    """

    name_resp = models.CharField(max_length=250, unique=True)  # описание обязанности

    def __str__(self):
        return f"name_resp: {self.name_resp}"


class Requirements(models.Model):
    """
    Класс «Требования» представляет собой модель хранения и управления требованиями с уникальным именем.
    """

    name_req = models.CharField(max_length=250, unique=True)  # описание требований

    def __str__(self):
        return f"name_req: {self.name_req}"


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

    date_cust = models.DateTimeField("Дата поступления вакансии", auto_now_add=True)
    employer = models.ForeignKey(Customer, on_delete=models.PROTECT)

    recruter = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="user_recruter"
    )

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="user_customer"
    )

    name_vacancy = models.CharField("Название вакансии", max_length=250)
    description_vacancy = models.TextField("Описание вакансии")
    region = models.CharField("Место работы", max_length=250)

    status_vacancy = models.IntegerField(
        "Статус вакансии", choices=VACANCY_STATUS, default=1
    )

    salary1 = models.IntegerField("Зарплата (нижняя планка)", default=0)
    salary2 = models.IntegerField("Зарплата (верхняя планка)", default=0)
    motivation = models.IntegerField("Дополнительная мотивация (Сумма)", default=0)
    avto = models.BooleanField("Наличие автомобиля", default=False)
    gsm = models.IntegerField("Расходы на топливо", default=0)
    substitute = models.BooleanField("Подменный сотрудник", default=False)
    type_job = models.BooleanField("Удаленная работа", default=False)
    intern = models.IntegerField("Вид стажировки", choices=INTERN_TYPE, default=1)
    schedule = models.CharField("График работы", max_length=30)
    count_hours = models.IntegerField("Среднее количество часов в день")
    count_tt = models.IntegerField("Среднее количество ТТ в день")

    responsibilities = models.ManyToManyField(
        Responsibilities, related_name="vacancy_resp"
    )

    requirements = models.ManyToManyField(Requirements, related_name="vacancy_req")
    cause = models.CharField("Причина открытия вакансии", max_length=500)

    def __str__(self):
        return f"id: {self.pk}, name_vacancy: {self.name_vacancy}"


class Candidate(models.Model):
    """
    Класс «Кандидат» представляет кандидата на должность и содержит различные поля, такие как имя,
    фамилия, дата рождения, адрес электронной почты, номер телефона и т. д.
    """

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    surname = models.CharField("Фамилия", max_length=20)
    name = models.CharField("Имя", max_length=20)
    otch = models.CharField("Отчество", max_length=20, null=True)
    birthday = models.DateField("Дата рождения")
    mail = models.EmailField("Почта")
    phone = models.CharField("Телефон", max_length=15)
    tlg = models.CharField("Телеграм", max_length=15)
    ref = models.TextField("Кто привел кандидата")
    auto = models.BooleanField("Наличие автомобиля", default=False)
    resume = models.FileField("Файл резюме", null=True)

    def __str__(self):
        return f"id: {self.pk}, name: {self.name}, surname: {self.surname}"


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

    candidat_id = models.ForeignKey(Candidate, on_delete=models.PROTECT)
    vacancy_id = models.ForeignKey(Vacancy, on_delete=models.PROTECT)

    status_change = models.IntegerField(
        "Текущий статус", choices=CANDIDATE_STATUS, default=1
    )

    status_change_date = models.DateTimeField(
        "Дата изменения статуса", auto_now_add=True
    )

    appointment_date = models.DateField("Назначенная дата")
    event = models.BooleanField("Состоялось событие", default=False)
    comment = models.TextField("Коментарий")


class Message(models.Model):
    """
    Класс, хранящий сведения о новых кандидатах и получателях сообщения
    """

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    candidate_id = models.ForeignKey(Candidate, on_delete=models.PROTECT)
    viewed = models.BooleanField("Просмотрено", default=False)
