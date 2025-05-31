"""
URL configuration for LabProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from . import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import routers,permissions
from lab.routers.routers import lab_routers
from servicemanagement.routers.router import service_router
from banner.routers.router import banner_router
from team.routers.router import team_router
from socialmedia.routers.router import socialMedia_router
from booking import urls as booking_urls
from booking.routers.router import Booking_router
from FAQS.routers.router import Faqs_router
from accounts.routers.router import Account_router
from logix.viewsets.viewset import RegisterView,LoginView
from rest_framework_simplejwt.views import (
    TokenObtainSlidingView,
    TokenRefreshSlidingView,
)
from logix.views import Login

router=routers.DefaultRouter()
router.registry.extend(lab_routers.registry)
router.registry.extend(service_router.registry)
router.registry.extend(banner_router.registry)
router.registry.extend(team_router.registry)
router.registry.extend(socialMedia_router.registry)
router.registry.extend(Booking_router.registry)
router.registry.extend(Faqs_router.registry)
router.registry.extend(Account_router.registry)


#swagger documetation:
schema_view=get_schema_view(
    openapi.Info(
        title="Lab API",
        default_version='v1',
        description="API for managing books",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="support@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    )



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('register',RegisterView.as_view(),name='register'),
    path('login',LoginView.as_view(),name='login'),
    path('api/token/', TokenObtainSlidingView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    # path('Lgn',views.Login),
]