from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Column, Team
from .serializers import ColumnSerializer

class ColumnViewSet(viewsets.ModelViewSet):
    serializer_class = ColumnSerializer

    def get_queryset(self):
        team_id = self.kwargs['team_id']
        return Column.objects.filter(team_id=team_id).order_by('order')

    def perform_create(self, serializer):
        team = Team.objects.get(id=self.kwargs['team_id'])
        serializer.save(team=team)