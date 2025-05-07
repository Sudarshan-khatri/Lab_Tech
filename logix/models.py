from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
class CustomUser(AbstractUser):
    Phone_number=PhoneNumberField(null=True,blank=True)
    is_lab_member=models.BooleanField(default=False)
