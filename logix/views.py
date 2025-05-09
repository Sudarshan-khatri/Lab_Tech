from django.shortcuts import render
from django.http import HttpResponse
from .email.emails import otp_generate 

# Create your views here.
def send_mail(request):
    OTP=otp_generate()
    if OTP:
        return HttpResponse(f'Delivery message:{OTP}')
    else:
        return HttpResponse(f"sorry failed to send mail")
