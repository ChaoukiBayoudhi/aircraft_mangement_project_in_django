from datetime import timedelta
from django.db.models import QuerySet
from django.utils import timezone
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets

from .enumerations import AircraftStatus
from .models import Aircraft, Flight, CrewMember, FlightCrewMember
from .serializers import AircraftSerializer, FlightSerializer, CrewMemberSerializer, FlightCrewMemberSerializer

class AircraftViewSet(viewsets.ModelViewSet):
    queryset=Aircraft.objects.all()
    serializer_class=AircraftSerializer

    #get aircrafts by status (as path parameter)
    @action(detail=False, methods=['GET'],url_path='status/(?P<aircraft_status>[^/.]+)')
    def get_aircrafts_by_status(self, request, aircraft_status):
        qs=Aircraft.objects.filter(status=aircraft_status)
        if not qs.exists():
            return Response({"message":"No aircrafts found with the status"},status.HTTP_204_NO_CONTENT)
        aircrafts=AircraftSerializer(qs,many=True)
        return Response(aircrafts.data,status.HTTP_200_OK)
    
    @action(detail=False, methods=['GET'],url_path='price-range')
    def get_aircrafts_by_price_range(self, request):
        lprice=request.query_params.get("lprice")
        hprice=request.query_params.get("hprice")
        if not lprice or not hprice:
            return Response({"message":"Both lprice and hprice parameters are required"},status.HTTP_400_BAD_REQUEST)
        try:
            lprice = float(lprice)
            hprice = float(hprice)
        except ValueError:
            return Response({"message":"lprice and hprice must be valid numbers"},status.HTTP_400_BAD_REQUEST)
        qs=Aircraft.objects.filter(price__range=(lprice,hprice))
        if not qs.exists():
            return Response({"message":"No aircrafts found in the price range"},status.HTTP_204_NO_CONTENT)
        aircrafts=AircraftSerializer(qs,many=True)
        return Response(aircrafts.data,status.HTTP_200_OK)

    #update all aircrafts status to Retired if they are very old
    @action(detail=False, methods=['PUT','PATCH'],url_path='update-retired-aircrafts')
    def update_retired_aircrafts(self, request):
        qs:QuerySet=Aircraft.objects.filter(manufacturing_date__lt=timezone.now()-timedelta(days=3650))
        if not qs.exists():
            return Response({"message":"No aircrafts found to update"},status.HTTP_204_NO_CONTENT)
        qs.update(status=AircraftStatus.RETIRED)
        #or using save() method
        #for aircraft in qs:
        #    aircraft.status=AircraftStatus.RETIRED
        #    aircraft.save()
        return Response({"message":"All aircrafts status updated to Retired"},status.HTTP_200_OK)

class FlightViewSet(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer

    #update many Flights by sending list of new Flight values
    @action(detail=False, methods=['PUT','PATCH'],url_path='update-many-flights')
    def update_many_flights(self, request):
        flights=request.data.get("flights",[])
        if not flights:
            return Response({"message":"No flights to update"},status.HTTP_400_BAD_REQUEST)
        for flight in flights:
            flight_number=flight.get("flight_number")
            if not flight_number:
                return Response({"message":"flight_number is required"},status.HTTP_400_BAD_REQUEST)
            try:
                flight_obj=Flight.objects.get(flight_number=flight_number)
            except Flight.DoesNotExist:
                return Response({"message":"Flight not found"},status.HTTP_404_NOT_FOUND)
            flight_obj.departure_airport=flight.get("departure_airport")
            #or without get() method
            flight_obj.departure_airport=flight["departure_airport"]

            flight_obj.arrival_airport=flight.get("arrival_airport")
            flight_obj.departure_time=flight.get("departure_time")
            flight_obj.arrival_time=flight.get("arrival_time")
            flight_obj.duration_hours=flight.get("duration_hours")
            flight_obj.distance_km=flight.get("distance_km")
            flight_obj.altitude_max=flight.get("altitude_max")
            flight_obj.status=flight.get("status")
            flight_obj.save()
        return Response({"message":"All flights updated successfully"},status.HTTP_200_OK)  

class CrewMemberViewSet(viewsets.ModelViewSet):
    queryset=CrewMember.objects.all()
    serializer_class=CrewMemberSerializer

class FlightCrewMemberViewSet(viewsets.ModelViewSet):
    queryset=FlightCrewMember.objects.all()
    serializer_class=FlightCrewMemberSerializer
    