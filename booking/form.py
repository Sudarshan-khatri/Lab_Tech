from django import forms
from .models import BookingModel


class BookingForm(forms.ModelForm):
    class Meta:
        model=BookingModel
        fields = [
            'Full_name', 'Email', 'Phone_Number', 'Address', 'Gender',
             'Services', 'Payment_option',
            'Message', 'Appointment_Booked'
        ]
        widgets = {
          
            'Services': forms.CheckboxSelectMultiple(),  # allows multiple service selection
        }
