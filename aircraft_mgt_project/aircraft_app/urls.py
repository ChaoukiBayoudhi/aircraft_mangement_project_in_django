from rest_framework import routers
from django.urls import path,include

from .views import AircraftCommunicationViewSet, AircraftViewSet, CrewMemberViewSet, FlightCrewMemberViewSet, FlightViewSet, SensorViewSet

router=routers.DefaultRouter()

router.register(r'aircrafts', AircraftViewSet)
router.register(r'sensors', SensorViewSet)
router.register(r'flights', FlightViewSet)
router.register(r'crew-members', CrewMemberViewSet)
router.register(r'fligt-crew-member', FlightCrewMemberViewSet)
router.register(r'aircraft-communications',AircraftCommunicationViewSet)

urlpatterns=[
    path('',include(router.urls))
]


