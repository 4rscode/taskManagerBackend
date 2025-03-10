from django.db import models
from django.utils import timezone
from teams.models import Team

class Column(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="columns")
    status = models.CharField(max_length=100)  # Название колонки, например "To Do"
    order = models.IntegerField(default=0)      # Для сортировки колонок

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.status} ({self.team.name})"