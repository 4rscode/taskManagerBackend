from django.db import models
from django.utils import timezone

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Например, "team1", "team2"

    def __str__(self):
        return self.name