from rest_framework.routers import DefaultRouter
from booking.viewsets.viewset import BookingView


#make the router
Booking_router=DefaultRouter()
Booking_router.register('Booking',BookingView)