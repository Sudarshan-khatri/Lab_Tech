from rest_framework.routers import DefaultRouter
from lab.viewset.viewset import LabViewset

#create routers
lab_routers=DefaultRouter()
lab_routers.register('Lab',LabViewset)