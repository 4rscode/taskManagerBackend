# tasks/admin.py
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'completed', 'created_at')  # Используем name вместо title, completed вместо status
    list_filter = ('completed', 'column')               # Фильтруем по completed и column