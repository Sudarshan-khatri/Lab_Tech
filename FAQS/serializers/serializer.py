from rest_framework import serializers
from FAQS.models import FaqsModel
 
 
class FaqsSerializer(serializers.ModelSerializer):
    class Meta:
        model=FaqsModel
        fields='__all__'

