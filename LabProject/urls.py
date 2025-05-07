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
from logix.routers.router import logix_router
from logix.viewsets.viewset import LoginUser


router=routers.DefaultRouter()
router.registry.extend(lab_routers.registry)
router.registry.extend(service_router.registry)
router.registry.extend(banner_router.registry)
router.registry.extend(team_router.registry)
router.registry.extend(socialMedia_router.registry)
router.registry.extend(logix_router.registry)


#swagger documetation:
schema_view=get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v2',
        description="Test description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('login',LoginUser.as_view(),name='Login'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    

]
