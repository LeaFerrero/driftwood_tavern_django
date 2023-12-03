from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.

from .models import Menu

@admin.register(Menu)
class MenuAdmin(ModelAdmin):
    ...