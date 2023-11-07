from django.db import models
from datetime import datetime, date
from django.utils import timezone

# статус кандидата, в виде списка кортежей, отображается в виде поля выбора со списком
# в базе хранится порядковый номер элемента списка
CANDIDATE_STATUS = [
    # по умолчанию, присваивается кандидату, при создании кандидата
    (1, "Новый"),
    # количество записей с подобным статусом у одного кандидата, соответствует количеству звонков
    (2, "Созвон"),
    # после трех недозвонов
    (3, "3-й недозвон"),
    # после удачного созвона, кандидат направляет резюме
    (4, "Резюме"),
    # одобрив резюме, кандидат поступает на стажировку
    (5, "Стажировка"),
    # пройдя стажировку, кандидат оформляется
    (6, "Оформление"),
    # заказчик на любой стадии может отказать кандидату, 3 недозвона, не пришел на стажировку и т.д.
    (7, "Отказ"),
    # имеются несколько кандидатов, удовлетворяющих требованиям заказчика
    (8, "Кадровый резерв"),
]

# статус вакансии, в виде списка кортежей, отображается в виде поля выбора со списком
# в базе хранится порядковый номер элемента списка
VACANCY_STATUS = [
    # по умолчанию, присваивается вакансии, при создании кандидата
    (1, "Открыта"),
    # кандидат подобран
    (2, "Закрыта"),
    (3, "Приостановлена"),
]

# вид стажировки, в виде списка кортежей, отображается в виде поля выбора со списком
# в базе хранится порядковый номер элемента списка
INTERN_TYPE = [
    (1, "Наставник"),
    (2, "Мерчендайзер"),
    (3, "Супервайзер"),
    (4, "Удаленно"),
]


class Customer(models.Model):
    """
    Класс «Клиент» представляет клиента с различными атрибутами, такими как
    название компании, описание, адреса, ИНН, текущий счет, телефон и адрес электронной почты.
    """

    company_name = models.CharField(
        "Название организации", max_length=30
    )  # краткое название фирмы
    description = models.TextField(
        "Описание организации"
    )  # описание организации - заказчика
    legal_address = models.CharField(
        "Юридический адрес", max_length=250
    )  # юридический адрес заказчика
    mailing_address = models.CharField(
        "Почтовый адрес", max_length=250
    )  # почтовый адрес заказчика
    inn = models.CharField("ИНН", max_length=10)  # ИНН заказчика
    checking_account = models.CharField(
        "Расчетный счет", max_length=20
    )  # расчетный счет заказчика
    phone = models.CharField("Телефон", max_length=15)  # телефон заказчика
    email = models.EmailField("Электронная почта")  # поле электронной почты заказчика

    def __str__(self):
        return f"customer: {self.name_customer}"


class Users(models.Model):
    """
    Класс Users представляет пользователя с такими атрибутами, как фамилия, имя, дата, день рождения,
    адрес электронной почты, телефон, tlg и ссылка на внешний ключ организации-клиента.
    """

    surname = models.CharField("Фамилия", max_length=20)
    name = models.CharField("Имя", max_length=20)
    otch = models.CharField("Отчество", max_length=20, null=True)
    birthday = models.DateField("Дата рождения")
    email = models.EmailField("Почта")
    phone = models.CharField("Телефон", max_length=15)
    tlg = models.CharField("Телеграм", max_length=15)
    customer = models.ForeignKey(
        Customer, on_delete=models.PROTECT, null=True
    )  # ссылка на организацию - заказчика, в которой работает пользователь,
    # если пустое, то Рекрут

    def __str__(self):
        return f"id: {self.pk}, name: {self.name}, surname: {self.surname}"


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

    date_cust = models.DateTimeField(
        "Дата поступления вакансии", auto_now_add=True
    )  # дата поступления / создания вакансии
    employer = models.ForeignKey(
        Customer, on_delete=models.PROTECT
    )  # организация - работодатель - заказчик
    recruter = models.ForeignKey(
        Users, on_delete=models.PROTECT, related_name="user_recruter"
    )  # рекрутер, ведущий вакансию
    customer = models.ForeignKey(
        Users, on_delete=models.PROTECT, related_name="user_customer"
    )  # сотрудник заказчика, ответственный за вакансию
    name_vacancy = models.CharField(
        "Название вакансии", max_length=30
    )  # краткое название вакансии
    description_vacancy = models.TextField("Описание вакансии")  # описание вакансии
    region = models.CharField(
        "Место работы", max_length=250
    )  # регион в котором находится вакансия
    status_vacancy = models.IntegerField(
        "Статус вакансии", choices=VACANCY_STATUS, default=1
    )  # поле выбора статуса вакансии,
    # из списка, по умолчанию статус вакансии - Открыта
    salary1 = models.IntegerField("Зарплата (нижняя планка)", default=0)
    salary2 = models.IntegerField("Зарплата (верхняя планка)", default=0)
    motivation = models.IntegerField("Дополнительная мотивация (Сумма)", default=0)
    auto = models.BooleanField("Наличие автомобиля", default=False)
    gsm = models.IntegerField("Расходы на топливо", default=0)
    substitute = models.BooleanField("Подменный сотрудник", default=False)
    type_job = models.BooleanField("Удаленная работа", default=False)
    intern = models.IntegerField("Вид стажировки", choices=INTERN_TYPE, default=1)
    schedule = models.CharField(
        "График работы", max_length=30
    )  # график работы, вручную
    count_hours = models.IntegerField("Среднее количество часов в день")
    count_tt = models.IntegerField("Среднее количество ТТ в день")
    responsibilities = models.ManyToManyField(
        Responsibilities, related_name="vacancy_resp"
    )  # обязанности
    requirements = models.ManyToManyField(
        Requirements, related_name="vacancy_req"
    )  # требования
    cause = models.CharField("Причина открытия вакансии")  # Причина открытия вакансии

    def __str__(self):
        return f"id: {self.pk}, name_vacancy: {self.name_vacancy}"


class Candidate(models.Model):
    """
    Класс «Кандидат» представляет кандидата на должность и содержит различные поля, такие как имя,
    фамилия, дата рождения, адрес электронной почты, номер телефона и т. д.
    """

    user_id = models.ForeignKey(
        Users, on_delete=models.PROTECT
    )  # рекрутер или заказчик, ведущий кандидата
    surname = models.CharField("Фамилия", max_length=20)
    name = models.CharField("Имя", max_length=20)
    otch = models.CharField("Отчество", max_length=20, null=True)
    birthday = models.DateField("Дата рождения")  # дата рождения
    mail = models.EmailField("Почта")  # поле электронной почты
    phone = models.CharField("Телефон", max_length=15)
    tlg = models.CharField("Телеграм", max_length=15)
    ref = models.TextField("Кто привел кандидата")  # если кандидата кто-то привел
    avto = models.BooleanField("Наличие автомобиля", default=False)

    def __str__(self):
        return f"id: {self.pk}, name: {self.name}, surname: {self.surname}"


class CandidatePromotion(models.Model):
    """
    Класс CandidatePromotion представляет продвижение кандидата на конкретную вакансию, включая такую
    информацию, как идентификаторы кандидата и вакансии, изменение статуса, дата изменения статуса, дата
    назначения, статус события и комментарий.
    """

    candidat_id = models.ForeignKey(
        Candidate, on_delete=models.PROTECT
    )  # ссылка на кандидата
    vacancy_id = models.ForeignKey(
        Vacancy, on_delete=models.PROTECT
    )  # ссылка на вакансию
    status_change = models.IntegerField(
        "Текущий статус", choices=CANDIDATE_STATUS, default=1
    )
    status_change_date = models.DateTimeField(
        "Дата изменения статуса", auto_now_add=True
    )  # автоматически
    appointment_date = models.DateField(
        "Назначенная дата"
    )  # Дата на которую назначено действие, согласно статуса (звонок, встреча)
    event = models.BooleanField(
        "Состоялось событие", default=False
    )  # состоялось ли событие (звонок, встреча)
    comment = models.TextField("Коментарий")
