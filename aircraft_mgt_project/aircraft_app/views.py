from rest_framework import viewsets
from .models import Aircraft, Sensor, Flight, CrewMember, Certification, MaintenanceRecord, FlightCrewMember 
from .serializers import AircraftSerializer, SensorSerializer, FlightSerializer, CrewMemberSerializer, CertificationSerializer, MaintenanceRecordSerializer, FlightCrewMemberSerializer

class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class CrewMemberViewSet(viewsets.ModelViewSet):
    queryset = CrewMember.objects.all()
    serializer_class = CrewMemberSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class MaintenanceRecordViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer


class FlightCrewMemberViewSet(viewsets.ModelViewSet):
    queryset = FlightCrewMember.objects.all()
    serializer_class = FlightCrewMemberSerializer
    