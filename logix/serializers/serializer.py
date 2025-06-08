from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password']

    def create(self,validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
    


class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(required=True)
    password=serializers.CharField(required=True)



class ResetPasswordSerializer(serializers.Serializer):
    email=serializers.EmailField(required=True)


    def validate_email(self,value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError('No user with this email')
        return value
    
class ResetPasswordConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(min_length=8)
    confirm_password = serializers.CharField(min_length=8)