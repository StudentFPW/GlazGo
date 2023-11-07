from django.contrib import admin

from notification.models import Message


@admin.register(Message)
class CustomerAdmin(admin.ModelAdmin):
    pass
