from rest_framework import serializers
from ..models import Team

class ListTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields=['Full_name','Email','Phone','Role','is_active','joined_date']


class RetrieveTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields=['Full_name','Email','Phone','Role','lab','is_active']


class WriteTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields='__all__'