from rest_framework import serializers
from ..models import CustomUser


class LoginUser(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['username','password']
     



class RegisterUser(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','username','email','password','phone_number','is_lab_member']
        extra_kwargs= {'password': {'write_only': True}}


    def create(self, validated_data):
        user=CustomUser(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
