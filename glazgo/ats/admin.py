from django.contrib import admin

from .models import *

admin.site.register(CPHistory)
admin.site.register(Vacancy)
admin.site.register(Candidate)
admin.site.register(CandidatePromotion)
admin.site.register(Message)
admin.site.register(CallCandidate)
admin.site.register(CandidateBase)
