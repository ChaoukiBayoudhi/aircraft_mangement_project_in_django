from django.db import models
class CrewMemberRole(models.TextChoices): 
    PILOT=    'PIL', 'Pilot'
    COPILOT=    'COP', 'Co-Pilot'
    ENGINEER=    'ENG', 'Engineer'
    FLIGHT_ATTENDANT=    'ATT', 'Flight Attendant'
    MAINTENANCE_TECHNICIAN=    'MT', 'Maintenance Technician'
    SECURITY_PERSONNEL=    'SP', 'Security Personnel'
    OTHER=    'OTHER', 'Other'

class AircraftType(models.TextChoices):
    COMMERCIAL = 'Commercial','Commercial Aircraft'
    PRIVATE = 'Private','Private Aircraft'
    MILITARY = 'Military','Military Aircraft'
    CARGO = 'Cargo','Cargo Aircraft'
    OTHER = 'Other','Other'

class AircraftStatus(models.TextChoices):
    ACTIVE = 'Active','Active'
    INACTIVE = 'Inactive','Inactive'
    MAINTENANCE = 'Maintenance','Maintenance'
    STORAGE = 'Storage','Storage'
    RETIRED = 'Retired','Retired'
    OTHER = 'Other','Other'

class SensorType(models.TextChoices):
    GPS = 'GPS', 'GPS'
    ALT = 'ALT', 'Alimeter'
    SPD = 'SPD', 'Speedometer'

class SensorStatus(models.TextChoices):
    ACTIVE = 'ACT', 'Active'
    CALIBRATED = 'CAL', 'Calibrated'
    ERROR = 'ERR', 'Error'

class CommunicationType(models.TextChoices):
    RADIO = 'RAD', 'Radio'
    DATA_LINK = 'DAT', 'Data Link'
    SATELLITE = 'SAT', 'Satellite'

class FlightPhase(models.TextChoices):
    TAXI = 'TAX', 'Taxi'
    TAKEOFF = 'TOF', 'Takeoff'
    CRUISE = 'CRU', 'Cruise'
    LANDING = 'LAN', 'Landing'

class FlightStatus(models.TextChoices):
    SCHEDULED = 'SCHED', 'Scheduled'
    BOARDING = 'BOARD', 'Boarding'
    IN_FLIGHT = 'INFLT', 'In Flight'
    DELAYED = 'DELAY', 'Delayed'
    CANCELLED = 'CANC', 'Cancelled'
    ARRIVED = 'ARRVD', 'Arrived'

class MaintenanceStatus(models.TextChoices):
    OPEN = 'OPEN', 'Open'
    IN_PROGRESS = 'INPR', 'In Progress'
    COMPLETED = 'COMP', 'Completed'
    DEFERRED = 'DEFR', 'Deferred'

class PartCategory(models.TextChoices):
    ENGINE = 'ENG', 'Engine'
    AVIONICS = 'AVN', 'Avionics'
    AIRFRAME = 'AIR', 'Airframe'
    ELECTRICAL = 'ELE', 'Electrical'
    INTERIOR = 'INT', 'Interior'
    OTHER = 'OTH', 'Other'

class SeverityLevel(models.TextChoices):
    MINOR = 'MIN', 'Minor'
    MAJOR = 'MAJ', 'Major'
    CRITICAL = 'CRI', 'Critical'

class FuelType(models.TextChoices):
    JET_A1 = 'JET', 'Jet A-1'
    AVGAS = 'AVG', 'Avgas'
    DIESEL = 'DSL', 'Diesel'

class WorkOrderPriority(models.TextChoices):
    LOW = 'LOW', 'Low'
    MEDIUM = 'MED', 'Medium'
    HIGH = 'HIGH', 'High'
    
    