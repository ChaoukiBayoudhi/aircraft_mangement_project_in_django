from django.contrib import admin
from .models import Aircraft, Sensor, Flight, CrewMember, Certification, MaintenanceRecord, FlightCrewMember, AircraftCommunication

admin.site.register(Aircraft)
admin.site.register(Sensor)
admin.site.register(Flight)
admin.site.register(CrewMember)
admin.site.register(Certification)
admin.site.register(MaintenanceRecord)
admin.site.register(FlightCrewMember)
admin.site.register(AircraftCommunication)