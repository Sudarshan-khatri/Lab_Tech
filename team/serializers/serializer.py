from rest_framework import serializers
from ..models import Team

class ListTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields= '__all__'


class RetrieveTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields=['TeamName', 'Team_member','Email','Phone','Role','lab','is_active']


class WriteTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields='__all__'