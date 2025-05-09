from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from ..serializers.serializer import FaqsSerializer
from ..models import FaqsModel


class FaqsView(viewsets.ModelViewSet):
    queryset=FaqsModel.objects.all().order_by('-id')
    permission_classes=[AllowAny]
    serializer_class=FaqsSerializer


