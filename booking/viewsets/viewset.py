from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from booking.serializers.serializer import ListBookingSerializer,RetrieveBookingSerializer,WriteBookingSerializer
from ..models import BookingModel
from ..form import BookingForm


class BookingView(viewsets.ModelViewSet):
    queryset=BookingModel.objects.all().order_by('-id')
    serializer_class=ListBookingSerializer
    # renderer_classes=[TemplateHTMLRenderer]
    # template_name=BookingForm


    

    def get_serializer_class(self):
        if self.action in ['create','update','partial_update']:
            return WriteBookingSerializer
        elif self.action=='retrieve':
            return RetrieveBookingSerializer
        return super().get_serializer_class()