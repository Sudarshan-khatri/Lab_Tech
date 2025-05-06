from rest_framework import viewsets
from banner.serializers.serializer import ListBannerSerializer,RetrieveBannerSerializer,writeBannerSerializer
from ..models import Banner

class BannerViewset(viewsets.ModelViewSet):
    queryset=Banner.objects.all()
    serializer_class=ListBannerSerializer

    def get_queryset(self):
        queryset=super().get_queryset()
        return queryset
    


    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return writeBannerSerializer
        elif self.action =='retrieve':
            return RetrieveBannerSerializer
        return super().get_serializer_class()