from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .enumerations import AircraftType, AircraftStatus, CrewMemberRole, SensorType, SensorStatus, CommunicationType, FlightPhase, FlightStatus, MaintenanceStatus, PartCategory, SeverityLevel, FuelType, WorkOrderPriority
from django.contrib.auth.models import User


class Aircraft(models.Model):
    registration_number = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255, unique=True)
    aircraft_type = models.CharField(max_length=255, 
                        choices=AircraftType.choices, 
                        default=AircraftType.PRIVATE
                        )
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='aircrafts/', null=True, blank=True)
    #auto_now_add=True means the date will be set to the current when the object is created
    manufacturing_date = models.DateField(auto_now_add=True)
    fuel_capacity = models.DecimalField(max_digits=10, decimal_places=2)
    max_speed=models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(3000)])
    satus=models.CharField(max_length=255, choices=AircraftStatus.choices, default=AircraftStatus.ACTIVE)
    class Meta:
        db_table='aircraft'
        ordering=['name','-model']
    
#----------sensor Model---------------

class Sensor(models.Model):
    name=models.CharField(max_length=100)
    sensor_type=models.CharField(max_length=3,choices=SensorType.choices)
    anufacturer = models.CharField(max_length=100)
    model_number = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50, unique=True)
    min_value = models.DecimalField(max_digits=10, decimal_places=2)
    max_value = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)
    accuracy = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=3, choices=SensorStatus.choices)
    last_calibration=models.DateTimeField(null=True, blank=True)
    next_calibration=models.DateTimeField(null=True,blank=True)
    #relationship between sensor and aircraft (*-1)
    aircraft=models.ForeignKey(Aircraft,on_delete=models.SET_NULL,
                                null=True,blank=True)

    
#---------------communication model----------
class Communication(models.Model):
    communication_type=models.CharField(max_length=3,choices=CommunicationType.choices)
    sender=models.CharField(max_length=100)
    receiver=models.CharField(max_length=100)
    message_content=models.TextField()
    flight_phase=models.CharField(max_length=3,choices=FlightPhase.choices)
    altitude = models.PositiveIntegerField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    frequency = models.DecimalField(max_digits=6, decimal_places=2)
    signal_strength = models.DecimalField(max_digits=6, decimal_places=2)
    timestamp = models.DateTimeField()
    duration_seconds = models.PositiveIntegerField(null=True, blank=True)
    #relationship between communication and aircraft[* - *] through the association class AircraftCommunication
    aircraft_communications=models.ManyToManyField(Aircraft,
                                                  through='AircraftCommunication',
                                                  through_fields=('communication','aircraft')
                                                )
    

    
#---------------flight model ------------

class Flight(models.Model):
    flight_number=models.CharField(max_length=20,unique=True)
    departure_airport=models.CharField(max_length=10)
    arrival_airport=models.CharField(max_length=10)
    departure_time=models.DateTimeField()
    arrival_time=models.DateTimeField()
    duration_hours=models.DecimalField(max_digits=5,decimal_places=2)
    distance_km=models.PositiveIntegerField()
    altitude_max=models.PositiveIntegerField()
    status=models.CharField(max_length=5, choices=FlightStatus.choices)
    #relationship between flight and aircraft[* - 1]
    aircraft=models.ForeignKey(Aircraft,on_delete=models.SET_NULL,
                                related_name='aircraft_flights',null=True, blank=True)
    
# -------------- Certification Model-------------
class Certification(models.Model):
    name = models.CharField(max_length=100)
    issuing_authority = models.CharField(max_length=100)
    valid_from = models.DateField()
    valid_until = models.DateField()

    
#------------ CrewMember model-----------

class  CrewMember(models.Model):
    employee_id=models.CharField(max_length=20,unique=True)
    
    role=models.CharField(max_length=10,choices=CrewMemberRole.choices)
    hire_date=models.DateField()
    certifications = models.ManyToManyField(Certification, related_name='crew_members')
    total_flight_hours = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=20)
    emergency_contact = models.CharField(max_length=100)
    emergency_phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    #relationship between crew member and User model(defined by Django)[1-1]
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='crew_member')
    #relationship between crew member and certification[* - *]
    certifications=models.ManyToManyField(Certification,
                                          blank=True,
                                            related_name='crew_member_certifications')
    active_certifications = models.ManyToManyField(Certification,
                                               blank=True,
                                               related_name='crew_member_active_certifications')
    unavailability_dates=models.JSONField(default=list)

#Association class between aircraft and communication for history tracking
class AircraftCommunication(models.Model):
    aircraft=models.ForeignKey(Aircraft,on_delete=models.SET_NULL,
                                related_name='communication_aircraft',null=True, blank=True)
    communication=models.ForeignKey(Communication,on_delete=models.SET_NULL,
                                    related_name='communication_history',null=True, blank=True)
    duration=models.DurationField()
    satart_date_time=models.DateTimeField(auto_now=True)

#Association class between flight and crew member
class FlightCrewMember(models.Model):
    flight=models.ForeignKey(Flight,on_delete=models.SET_NULL,
                            related_name='crew_members',null=True, blank=True, unique=True)
    crew_member=models.ForeignKey(CrewMember,on_delete=models.SET_NULL,
                                related_name='flight_crew_members',null=True, blank=True)
    role=models.CharField(max_length=10,choices=CrewMemberRole.choices)
    start_time=models.DateTimeField()
    duration=models.DurationField()
    class Meta:
        pass
    
    
# ---------------- Additional domain models ----------------

class Airport(models.Model):
    iata_code = models.CharField(max_length=3, unique=True)
    icao_code = models.CharField(max_length=4, unique=True, null=True, blank=True)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

class Route(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name='routes_originating')
    destination = models.ForeignKey(Airport, on_delete=models.PROTECT, related_name='routes_destination')
    distance_km = models.PositiveIntegerField()
    is_international = models.BooleanField(default=False)

class FlightPlan(models.Model):
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE, related_name='plan')
    route = models.ForeignKey(Route, on_delete=models.PROTECT, related_name='flight_plans', null=True, blank=True)
    filed_time = models.DateTimeField()
    alternate_airport = models.ForeignKey(Airport, on_delete=models.SET_NULL, null=True, blank=True, related_name='alternate_for')
    cruising_altitude_ft = models.PositiveIntegerField()
    fuel_required_kg = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField(blank=True)

class WeatherReport(models.Model):
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='weather_reports')
    timestamp = models.DateTimeField()
    temperature_c = models.DecimalField(max_digits=4, decimal_places=1)
    wind_speed_kt = models.DecimalField(max_digits=5, decimal_places=1)
    visibility_km = models.DecimalField(max_digits=4, decimal_places=1)
    metar = models.TextField()

class MaintenanceTask(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    estimated_hours = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(0)])
    category = models.CharField(max_length=3, choices=PartCategory.choices, default=PartCategory.OTHER)

class MaintenanceRecord(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name='maintenance_records')
    work_order_number = models.CharField(max_length=30, unique=True)
    status = models.CharField(max_length=4, choices=MaintenanceStatus.choices, default=MaintenanceStatus.OPEN)
    priority = models.CharField(max_length=4, choices=WorkOrderPriority.choices, default=WorkOrderPriority.MEDIUM)
    tasks = models.ManyToManyField(MaintenanceTask, related_name='work_orders', blank=True)
    opened_at = models.DateTimeField(auto_now_add=True)
    closed_at = models.DateTimeField(null=True, blank=True)
    performed_by = models.ManyToManyField(CrewMember, related_name='maintenance_performed', blank=True)
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes = models.TextField(blank=True)

class Part(models.Model):
    part_number = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=3, choices=PartCategory.choices, default=PartCategory.OTHER)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField(default=0)

class PartInstallation(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name='part_installations')
    part = models.ForeignKey(Part, on_delete=models.CASCADE, related_name='installations')
    installed_on = models.DateTimeField()
    removed_on = models.DateTimeField(null=True, blank=True)
    hours_used = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0)])

class FuelLog(models.Model):
    aircraft = models.ForeignKey(Aircraft, on_delete=models.CASCADE, related_name='fuel_logs')
    fuel_type = models.CharField(max_length=3, choices=FuelType.choices, default=FuelType.JET_A1)
    quantity_liters = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    supplier = models.CharField(max_length=100)
    refueled_at = models.DateTimeField()

class IncidentReport(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.SET_NULL, null=True, blank=True, related_name='incidents')
    aircraft = models.ForeignKey(Aircraft, on_delete=models.SET_NULL, null=True, blank=True, related_name='incidents')
    reported_by = models.ForeignKey(CrewMember, on_delete=models.SET_NULL, null=True, blank=True, related_name='incident_reports')
    severity = models.CharField(max_length=3, choices=SeverityLevel.choices)
    occurred_at = models.DateTimeField()
    location_description = models.CharField(max_length=200, blank=True)
    description = models.TextField()
    corrective_action = models.TextField(blank=True)
    
    