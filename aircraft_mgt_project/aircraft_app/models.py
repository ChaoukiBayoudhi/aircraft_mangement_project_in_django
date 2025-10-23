from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class AircraftType(models.TextChoices):
    COMMERCIAL = 'Commercial','Commercial Aircraft'
    PRIVATE = 'Private','Private Aircraft'
    MILITARY = 'Military','Military Aircraft'
    CARGO = 'Cargo','Cargo Aircraft'

class AircraftStatus(models.TextChoices):
    ACTIVE = 'Active','Active'
    INACTIVE = 'Inactive','Inactive'
    MAINTENANCE = 'Maintenance','Maintenance'
    STORAGE = 'Storage','Storage'
    RETIRED = 'Retired','Retired'
    OTHER = 'Other','Other'

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
    
#----------sensor Model---------------

class Sensor(models.Model):
    name=models.CharField(max_length=100)
    sensor_type_choices=[('GPS','GPS'),('ALT','Alimeter'),('SPD','Speedometer')]
    sensor_type=models.CharField(max_length=3,choices=sensor_type_choices)
    anufacturer = models.CharField(max_length=100)
    model_number = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=50, unique=True)
    min_value = models.DecimalField(max_digits=10, decimal_places=2)
    max_value = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=20)
    accuracy = models.DecimalField(max_digits=5, decimal_places=2)
    STATUS_CHOICES = [('ACT', 'Active'),('CAL', 'Calibrated'),('ERR', 'Error')]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    last_calibration=models.DateTimeField(null=True, blank=True)
    next_calibration=models.DateTimeField(null=True,blank=True)
    #relationship between sensor and aircraft (*-1)
    aircraft=models.ForeignKey(Aircraft,on_delete=models.SET_NULL,
                                null=True,blank=True)

    
#---------------communication model----------
class communication(models.Model):
    COMM_TYPES = [
        ('RAD', 'Radio'),
        ('DAT', 'Data Link'),
        ('SAT', 'Satellite'),
    ]

    FLIGHT_PHASE_CHOICES = [
        ('TAX', 'Taxi'),
        ('TOF', 'Takeoff'),
        ('CRU', 'Cruise'),
        ('LAN', 'Landing'),
    ]
    communication_type=models.CharField(max_length=3,choices=COMM_TYPES)
    sender=models.CharField(max_length=100)
    receiver=models.CharField(max_length=100)
    message_content=models.TextField()
    flight_phase=models.CharField(max_length=3,choices=FLIGHT_PHASE_CHOICES)
    altitude = models.PositiveIntegerField(null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    frequency = models.DecimalField(max_digits=6, decimal_places=2)
    signal_strength = models.DecimalField(max_digits=6, decimal_places=2)
    timestamp = models.DateTimeField()
    duration_seconds = models.PositiveIntegerField(null=True, blank=True)

    
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
    status=models.CharField()
    def __str__(self):
        return f"{self.flight_number} ({self.aircraft.registration_number})"
    

# -------------- Certification Model-------------
class Certification(models.Model):
    name = models.CharField(max_length=100)
    issuing_authority = models.CharField(max_length=100)
    valid_from = models.DateField()
    valid_until = models.DateField()

    
#------------ CrewMember model-----------

class  CrewMember(models.Model):
    employee_id=models.CharField(max_length=20,unique=True)
    role_choices = [
        ('PIL', 'Pilot'),
        ('COP', 'Co-Pilot'),
        ('ENG', 'Engineer'),
        ('ATT', 'Flight Attendant'),
    ]
    role=models.CharField(max_length=10,choices=role_choices)
    hire_date=models.DateField()
    certifications = models.ManyToManyField(Certification, related_name='crew_members')
    total_flight_hours = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=20)
    emergency_contact = models.CharField(max_length=100)
    emergency_phone = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)

    