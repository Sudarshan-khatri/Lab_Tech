from rest_framework import viewsets
from team.serializers.serializer import ListTeamSerializer,RetrieveTeamSerializer,WriteTeamSerializer
from ..models import Team

class TeamViewset(viewsets.ModelViewSet):
    queryset=Team.objects.all()
    serializer_class=ListTeamSerializer

    def get_queryset(self):
        return super().get_queryset()
    
    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return WriteTeamSerializer
        elif self.action=='retrieve':
            return RetrieveTeamSerializer
        return super().get_serializer_class()