from django.contrib import admin

from .models import *
from users.models import Users

admin.site.register(Customer)
admin.site.register(Users)
admin.site.register(Responsibilities)
admin.site.register(Requirements)
admin.site.register(Vacancy)
admin.site.register(Candidate)
admin.site.register(CandidatePromotion)
admin.site.register(Message)
