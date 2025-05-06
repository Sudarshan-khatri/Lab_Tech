from django.db import models
import os

# Create your models here.
class Banner(models.Model):
    image=models.ImageField(upload_to='Banner/images/',null=True,blank=True)
    image_link=models.URLField(null=True,blank=True)
    video=models.FileField(upload_to='Banner/images/',null=True,blank=True)
    video_link=models.URLField(null=True,blank=True)


    created_date=models.DateField(auto_now_add=True,blank=True,null=True)
    updated_date=models.DateTimeField(auto_now=True,null=True,blank=True)



    def __str__(self):
        return f"Banner{self.id}"   
    

    def delete(self,*args,**kwargs):
        #remove the duplicate image:
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)

        #remove the duplicate video
        if self.video and os.path.isfile(self.video.path):
            os.remove(self.video.path)

        super().delete(*args,**kwargs)