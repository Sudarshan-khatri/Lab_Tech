from django.db import models

# Create your models here.
class Account(models.Model):
    Name=models.CharField(max_length=200,null=False)
    role=models.CharField(max_length=400,null=True,blank=True)
    lab=models.ManyToManyField('lab.LabModel',related_name='member')


    def __str__(self):
        return self.Name


