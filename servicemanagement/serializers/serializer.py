from rest_framework import serializers
from ..models import ServiceManagement

class ListServiceManagementSerializer(serializers.Serializer):
    class Meta:
        model=ServiceManagement
        fields=['name','category','price','Description']



class RetrieveServiceManagementSerializer(serializers.Serializer):
    class Meta:
        model=ServiceManagement
        fields=['name','category','Description']


class WriteServiceManagementSerializer(serializers.Serializer):
    class Meta:
        model=ServiceManagement
        fields='__all__'
