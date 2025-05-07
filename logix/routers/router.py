from rest_framework.routers import DefaultRouter
from logix.viewsets.viewset import RegisterViewset,LoginUser


#create the router path:
logix_router=DefaultRouter()
logix_router.register('Register',RegisterViewset)
