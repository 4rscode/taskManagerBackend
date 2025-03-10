from django.db import models
from django.utils import timezone
from columns.models import Column

class Task(models.Model):
    column = models.ForeignKey(Column, on_delete=models.CASCADE, related_name="tasks")
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, default="")
    due_date = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    assignees = models.JSONField(default=list)  # Список ответственных (например, ["Алексей"])
    images = models.JSONField(default=list)     # Список URL или base64 изображений
    order = models.IntegerField(default=0)       # Для сортировки задач
    created_at = models.DateTimeField(auto_now_add=True)  # Время создания

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name