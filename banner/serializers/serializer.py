from rest_framework import serializers
from ..models import Banner


class ListBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields='__all__'

class RetrieveBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields=['image','video']

class writeBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields='__all__'