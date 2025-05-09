from django.db import models

# Create your models here.
class FaqsModel(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField(max_length=6000,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated_date=models.DateTimeField(auto_now=True,null=True,blank=True)


    def __str__(self):
        return self.title
