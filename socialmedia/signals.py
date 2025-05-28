from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SocialMedia


@receiver(post_save,sender=SocialMedia)
def social_media(sender, instance, created, **kwargs):
    if created:
       print('Social media created sucessfully !!!!!!!!!!!!!!!')
