from rest_framework.routers import DefaultRouter
from banner.viewsets.viewset import BannerViewset

#register the router
banner_router=DefaultRouter()
banner_router.register('Banner',BannerViewset)