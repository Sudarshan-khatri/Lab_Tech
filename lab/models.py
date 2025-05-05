from django.db import models
import random


# Create your models here.
class LabModel(models.Model):
    lab_name=models.CharField(max_length=100,blank=True)
    location=models.CharField(max_length=200,blank=True)
    lab_code=models.CharField(max_length=200,blank=True,editable=False)
    lab_head=models.CharField(max_length=200)
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


    def __str__(self):
       return  self.lab_name, 
        