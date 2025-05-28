from rest_framework.routers import DefaultRouter
from accounts.viewsets.viewset import AccountView

#set the router 
Account_router=DefaultRouter()
Account_router.register('Account',AccountView)