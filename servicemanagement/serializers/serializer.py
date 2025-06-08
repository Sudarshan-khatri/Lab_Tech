from rest_framework import serializers
from ..models import ServiceManagement

class ListServiceManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceManagement
        fields= '__all__'



class RetrieveServiceManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceManagement
        fields=['Lab_name','category','Description']


class WriteServiceManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model=ServiceManagement
        fields='__all__'
