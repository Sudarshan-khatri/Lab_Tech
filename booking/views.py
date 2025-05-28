from django.shortcuts import render ,redirect
from .form import BookingForm

# Create your views here.

def book_appointment(request):
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success') 
        else:
            form = BookingForm()
        return render(request, 'Booking.booking.html', {'form': form})
