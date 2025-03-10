from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Task, Column
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        column_id = self.kwargs['column_id']
        return Task.objects.filter(column_id=column_id)

    def perform_create(self, serializer):
        column = Column.objects.get(id=self.kwargs['column_id'])
        serializer.save(column=column)