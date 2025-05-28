from rest_framework import serializers
from ..models import BookingModel


class ListBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookingModel
        fields='__all__'
class RetrieveBookingSerializer(serializers.Serializer):
    class Meta:
        model=BookingModel
        fields=['Full_name','Email','Phone_Number','Address','Gender','Appointment_Date','Services','Amount','Payment_status','Payment_option']


class WriteBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookingModel
        fields='__all__'

        