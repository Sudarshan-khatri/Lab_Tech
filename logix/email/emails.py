from django.core.mail import send_mail
from django.conf import settings
import random



def otp_generate():
    subject='Your otp is given:'
    otp=random.randint(1000,9999)
    message=f'Your otp is:{otp}'
    email_form=settings.EMAIL_HOST_USER
    recipient_list=['khatrisudarshan320@gmail.com']
    try:
        send_mail(subject,message,email_form,recipient_list)
        return otp
    except Exception as e:
        return f"Otp error as{e}"
