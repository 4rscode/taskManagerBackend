# teams/admin.py
from django.contrib import admin
from .models import Team

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Только name, так как других полей нет
    list_filter = ()          # Убираем фильтр, так как нет подходящих полей