from rest_framework import routers
from django.urls import path, include

from .views import AircraftViewSet, CrewMemberViewSet, FlightCrewMemberViewSet, FlightViewSet, SensorViewSet
router=routers.DefaultRouter()
router.register('aircrafts',AircraftViewSet)
router.register('sensors',SensorViewSet)
router.register('crew-members',CrewMemberViewSet)
router.register('flights',FlightViewSet)
router.register('flight-crew-members',FlightCrewMemberViewSet)

urlpatterns=[
    path('',include(router.urls))
]