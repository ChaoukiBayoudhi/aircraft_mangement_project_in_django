from django.contrib import admin

from .models import Aircraft, Flight, CrewMember, FlightCrewMember

# Register your models here.
admin.site.register(Aircraft)
admin.site.register(Flight)
admin.site.register(CrewMember)
admin.site.register(FlightCrewMember)
