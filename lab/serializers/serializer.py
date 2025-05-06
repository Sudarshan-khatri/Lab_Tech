from rest_framework import serializers
from ..models import LabModel

class ListLabModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=LabModel
        fields=['Branch_name','location','lab_code','lab_head','capacity','is_active','created_at','updated_at']


#serilaizer to retrieve the data
class RetrieveLabModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=LabModel
        fields=['lab_name','location','lab_head','capacity']

#serializer to write the data
class WriteLabModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=LabModel
        fields='__all__'