# Register your models here.
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from django_orm.models import User


@admin.register(User)
class User(ModelAdmin):
    pass
