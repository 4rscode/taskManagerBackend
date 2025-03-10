from rest_framework import serializers
from .models import Team
from columns.serializers import ColumnSerializer

class TeamSerializer(serializers.ModelSerializer):
    columns = ColumnSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'columns']