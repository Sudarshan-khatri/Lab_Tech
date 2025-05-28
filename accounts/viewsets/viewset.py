from rest_framework import viewsets
from accounts.models import Account
from rest_framework.permissions import AllowAny
from accounts.serializers.serializer import AccountSerializer

class AccountView(viewsets.ModelViewSet):
    queryset=Account.objects.all().order_by('-id')
    permission_classes=[AllowAny]
    serializer_class=AccountSerializer
