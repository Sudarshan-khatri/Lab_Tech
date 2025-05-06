from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class BookingModel(models.Model):
    gender_choice=[
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    ]
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('failed', 'Failed'),
    ]
    PAYMENT_METHOD_CHOICES = [
        ('esewa', 'eSewa'),
        ('khalti', 'Khalti'),
        ('cod', 'Cash on Delivery'),
    ]
    Appointment_Booked_choice=[
        ('Online','Online'),
        ('At_clinic','At clinic')
    ]
    Full_name=models.CharField(max_length=400,null=True)
    Email=models.EmailField(max_length=600,unique=True)
    Phone_Number=PhoneNumberField(blank=True)
    Address=models.CharField(max_length=200,blank=True)
    Gender=models.CharField(max_length=200,choices=gender_choice,default='Male')
    Appointment_Date=models.DateField(auto_now=True)
    Services=models.ForeignKey('servicemanagement.ServiceManagement',on_delete=models.CASCADE,blank=True,related_name='servicemgt')
    Amount=models.ForeignKey('servicemanagement.ServiceManagement',on_delete=models.CASCADE,related_name='service')
    Payment_status=models.CharField(max_length=200,choices=PAYMENT_STATUS_CHOICES,default='pending')
    Payment_option=models.CharField(max_length=200,choices=PAYMENT_METHOD_CHOICES,default='eSewa')
    Message=models.CharField(max_length=3000,blank=True)
    Appointment_Booked=models.CharField(max_length=200,choices=Appointment_Booked_choice,default='At clinic')



    def __str__(self):
        return self.Full_name