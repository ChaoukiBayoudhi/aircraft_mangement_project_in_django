from rest_framework import routers
#from django.urls import path, include
from .views import AircraftViewSet, CrewMemberViewSet, FlightCrewMemberViewSet, FlightViewSet
router=routers.DefaultRouter()
router.register('aircraft',AircraftViewSet)
router.register('Flight',FlightViewSet)
router.register('Crew-member',CrewMemberViewSet)
router.register('flight-crew-member',FlightCrewMemberViewSet)



urlpatterns = router.urls
#or
#urlpatterns = [
#    path('',include(router.urls)),
#]
