

from rest_framework import serializers
from .models import Aircraft, CrewMember, Flight, FlightCrewMember, Certification, Sensor, Part, Communication, AircraftCommunication


class AircraftSerializer(serializers.ModelSerializer):
    class Meta:
        model=Aircraft
        fields='__all__'
        #fields=['registration_number','name','model'] #only the fields you want to serialize

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Certification
        fields='__all__'

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sensor
        fields='__all__'

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Part
        fields='__all__'

class CommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Communication
        fields='__all__'

class AircraftCommunicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=AircraftCommunication
        fields='__all__'

class FlightCrewMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=FlightCrewMember
        fields='__all__'

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model=Flight
        fields='__all__'

class CrewMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model=CrewMember
        fields='__all__'

