from django.db import models
import random
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class LabModel(models.Model):
    Branch_type_choice=[
        ('Headquarter','Headquarter'),
        ('Other Branch','other Branch')
    ]
    Branch_name=models.CharField(max_length=100,unique=True,blank=True)
    Email=models.EmailField(max_length=300,unique=True, null=True, blank=True)
    Phone_number=PhoneNumberField(unique=True,blank=True)
    location=models.CharField(max_length=200,blank=True)
    lab_code=models.CharField(max_length=200,blank=True,editable=False)
    lab_head=models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=9, decimal_places=6,default=0.0)
    longitude = models.DecimalField(max_digits=9, decimal_places=6,default=0.0)
    Branch_type=models.CharField(max_length=200,choices=Branch_type_choice,blank=True)
    capacity=models.IntegerField()
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    
    #function to make the lab code
    def save(self,*arg,**kwargs):
        if not self.lab_code:
            #find uniqueness
            while True:
                code=f"GEN-{random.randint(1000, 9999)}"
                if not LabModel.objects.filter(lab_code=code).exists():
                    self.lab_code=code
                    break
        super().save(*arg,**kwargs)

    def save(self,*args,**kwargs):
       pass

    def __str__(self):
       return  self.Branch_name 
        