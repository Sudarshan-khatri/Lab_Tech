from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Team(models.Model):
    ROLE_CHOICES = [
        ('Technician', 'Technician'),
        ('Supervisor', 'Supervisor'),
        ('Assistant', 'Assistant'),
        ('Manager', 'Manager'),
        ('Admin', 'Admin'),
    ]
     
    TeamName=models.CharField(max_length=300,blank=True,null=True)
    Team_member=models.ManyToManyField('accounts.Account',null=True,blank=True)
    Email=models.EmailField(max_length=300,null=True,blank=True)
    Phone=PhoneNumberField(null=True,blank=True)
    Role=models.CharField(max_length=300,choices=ROLE_CHOICES,null=True)
    lab=models.ForeignKey('lab.LabModel',on_delete=models.CASCADE,null=True,related_name='team_member')
    is_active=models.BooleanField(default=True)
    joined_date=models.DateField(auto_now_add=True,null=True)

    def __str__(self):
        return self.TeamName
    

    


