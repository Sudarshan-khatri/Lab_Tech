from rest_framework.routers import DefaultRouter
from FAQS.viewsets.viewset import FaqsView


#set the router 
Faqs_router=DefaultRouter()
Faqs_router.register('FAQS',FaqsView)