from django.contrib import admin

from ats.models import Customer, Users, Responsibilities, Requirements, Vacancy, Candidate, CandidatePromotion


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass

@admin.register(Responsibilities)
class ResponsibilitiesAdmin(admin.ModelAdmin):
    pass

@admin.register(Requirements)
class RequirementsAdmin(admin.ModelAdmin):
    pass

@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass

@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    pass

@admin.register(CandidatePromotion)
class CandidatePromotionAdmin(admin.ModelAdmin):
    pass