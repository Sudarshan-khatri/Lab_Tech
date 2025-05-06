from rest_framework.routers import DefaultRouter
from socialmedia.viewsets.viewset import SocialMediaViewset


#define the router
socialMedia_router=DefaultRouter()
socialMedia_router.register('Social_Media',SocialMediaViewset)


