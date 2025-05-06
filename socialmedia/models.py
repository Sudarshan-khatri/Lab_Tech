from django.db import models

# Create your models here.
class SocialMedia(models.Model):
    Facebook=models.URLField(blank=True,null=True)
    You_Tube=models.URLField(blank=True,null=True)
    Instagram=models.URLField(blank=True,null=True)
    Twitter=models.URLField(blank=True,null=True)
    Linkden=models.URLField(blank=True,null=True)



    def __str__(self):
        return f"social media"
