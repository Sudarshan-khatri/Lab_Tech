from rest_framework.routers import DefaultRouter
from servicemanagement.viewsets.viewset import servicemgtViewset

service_router=DefaultRouter()
service_router.register('Service',servicemgtViewset,basename='service')