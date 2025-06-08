from rest_framework import generics
from django.contrib.auth.models import User
from logix.serializers.serializer import RegisterSerializer,LoginSerializer,UserSerializer,ResetPasswordSerializer,ResetPasswordConfirmSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import authenticate
from ..utilities.pagination import LogixPagination
from ..utilities.permission import IsAdmin,IsStaff,IsUser



class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    permission_classes=[AllowAny]
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
            return Response({
                'refresh':str(refresh),
                'access':str(refresh.access_token),
                'user':user_serializer.data,
                })
        return Response({'Message':'Invalid credential'},status=401)
    

class Reset_password(generics.CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class=ResetPasswordSerializer


    def post(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email=serializer.validated_data['email']
        user=User.objects.get(email=email)



        token_generator=PasswordResetTokenGenerator()
        token=token_generator.make_token(user)
        uid=urlsafe_base64_encode(force_bytes(user.pk))

        # reset_url=request.build_absolute_url(reverse('password-reset-confirm'),kwargs={'uidb64':uid,'token':token})
        reset_url = request.build_absolute_uri(reverse('password-reset-confirm', kwargs={'uidb64': uid, 'token': token}))


        send_mail(
            subject='Reset your password',
            message=f'Click the link to reset your password:{reset_url}',
            from_email='khatrisudarshan360@gmail.com',
            recipient_list=[user.email],
            fail_silently=False
        )

        return Response({'message':'Password reset link sent to your email'},status=200)
    
class ResetPasswordConfirmView(generics.CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class=ResetPasswordConfirmSerializer
 

    def post(self,request,uidb64,token,*args,**kwargs):
        try:
            uid=urlsafe_base64_decode(uidb64).decode()
            user=User.objects.get(pk=uid)
        except Exception:
            return Response({'error': 'Invalid link'}, status=400)
        
        token_generator=PasswordResetTokenGenerator()
        if not token_generator.check_token(user, token):
            return Response({'error': 'Token is invalid or has expired'}, status=400)
        

        new_password=request.data.get('new_password')
        confirm_password=request.data.get('confirm_password')


        if not new_password or new_password !=confirm_password:
            return Response({'message':'Password not match'},status=400)
        
        user.set_password(new_password)
        user.save()
        return Response({'message':'Password has been reset sucessfully'},status=200)
