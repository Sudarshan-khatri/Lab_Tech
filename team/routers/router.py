from rest_framework.routers import DefaultRouter
from team.viewsets.viewset import TeamViewset

#router of the team 
team_router=DefaultRouter()
team_router.register('Team_Member',TeamViewset)