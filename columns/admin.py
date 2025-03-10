# columns/admin.py
from django.contrib import admin
from .models import Column

@admin.register(Column)
class ColumnAdmin(admin.ModelAdmin):
    list_display = ('status', 'team', 'order')  # Поля для отображения в списке
    list_filter = ('team',)                     # Фильтр по команде
    search_fields = ('status',)                 # Поиск по статусу
    ordering = ('order',)                       # Сортировка по порядку