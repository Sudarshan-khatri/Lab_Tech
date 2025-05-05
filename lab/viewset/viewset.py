from rest_framework import viewsets
from ..models import LabModel 
from lab.serializers.serializer import ListLabModelSerializer,RetrieveLabModelSerializer,WriteLabModelSerializer


#class to set the view
class LabViewset(viewsets.ModelViewSet):
    queryset=LabModel.objects.all()
    serializer_class=WriteLabModelSerializer

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset
    

    def get_serializer_class(self):
        if self.action=='list':
            return ListLabModelSerializer
        elif self.action in ['create','partial_update','update']:
            return WriteLabModelSerializer
        elif self.action=='retrieve':
            return RetrieveLabModelSerializer
        return super().get_serializer_class()
    