from rest_framework import viewsets
from socialmedia.serializer.serializer import WriteSocialMedia
from socialmedia.models import SocialMedia


class SocialMediaViewset(viewsets.ModelViewSet):
    queryset=SocialMedia.objects.all()
    serializer_class=WriteSocialMedia
