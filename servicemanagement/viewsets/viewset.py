from rest_framework import viewsets  
from servicemanagement.serializers.serializer import ListServiceManagementSerializer,RetrieveServiceManagementSerializer,WriteServiceManagementSerializer
from ..models import ServiceManagement



class servicemgtViewset(viewsets.ModelViewSet):
    queryset=ServiceManagement.objects.all()
    serializer_class=WriteServiceManagementSerializer



    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset
    

    def get_serializer_class(self):
        if self.action=='list':
            return ListServiceManagementSerializer
        elif self.action in ['create','update','partial_update']:    
            return WriteServiceManagementSerializer
        elif self.action=='retrieve':
            return RetrieveServiceManagementSerializer
        return super().get_serializer_class()