from rest_framework import serializers
from ..models import SocialMedia



class WriteSocialMedia(serializers.ModelSerializer):
    class Meta:
        model=SocialMedia
        fields='__all__'

