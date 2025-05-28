from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import BookingModel

@receiver(post_save,sender=BookingModel)
def Send_message(sender,instance,created,**kwargs):
    if created:
        print("Booking sucessfull!!!!")
