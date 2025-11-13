from rest_framework import viewsets
from .models import Aircraft, AircraftCommunication, Sensor, Flight, CrewMember, Certification, MaintenanceRecord, FlightCrewMember 
from .serializers import AircraftCommunicationSerializer, AircraftSerializer, SensorSerializer, FlightSerializer, CrewMemberSerializer, CertificationSerializer, MaintenanceRecordSerializer, FlightCrewMemberSerializer
from rest_framework.decorators import action
class AircraftViewSet(viewsets.ModelViewSet):
    queryset = Aircraft.objects.all()
    serializer_class = AircraftSerializer
    @action(detail=False, methods=['get'], url_path='status/(?P<status>[^/.]+)')
    def get_aircrafts_by_status(self, request):
            pass

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

class AircraftCommunicationViewSet(viewsets.ModelViewSet):
    queryset = AircraftCommunication.objects.all()
    serializer_class = AircraftCommunicationSerializer

    