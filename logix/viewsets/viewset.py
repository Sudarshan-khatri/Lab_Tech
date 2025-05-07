from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from logix.serializers.serializer import LoginUser,RegisterUser
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from logix.models import CustomUser




class RegisterViewset(viewsets.ModelViewSet): 
    queryset=CustomUser.objects.all()
    serializer_class=RegisterUser



class LoginUser(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")
        user=authenticate(username=username,password=password)

        if user is not None:
            return Response({'message':'Login sucessfully'},status=status.HTTP_200_OK)
        else:
            return Response({'message':'Invalid Credential'},status=status.HTTP_401_UNAUTHORIZED)