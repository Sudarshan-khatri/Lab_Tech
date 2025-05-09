from rest_framework import generics
from django.contrib.auth.models import User
from logix.serializers.serializer import RegisterSerializer,LoginSerializer,UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from ..utilities.pagination import LogixPagination
from ..utilities.permission import IsAdmin,IsStaff,IsUser



class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes=[IsAdmin]
    serializer_class=RegisterSerializer
    pagination_class=LogixPagination


class LoginView(generics.CreateAPIView):
    serializer_class=LoginSerializer
    permission_classes=[AllowAny]

    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        print("USERNAME:", username)
        print("PASSWORD:", password)

        if not username or not password:
            return Response({'error': 'Username and password are required.'}, status=400)

        user=authenticate(username=username , password=password)


        if user is not  None:
            refresh=RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            role='admin' if user.is_superuser else 'staff' if user.is_staff else 'user'
            return Response({
                'refresh':str(refresh),
                'access':str(refresh.access_token),
                'user':user_serializer.data,
                'role':role
                })
        return Response({'Message':'Invalid credential'},status=401)