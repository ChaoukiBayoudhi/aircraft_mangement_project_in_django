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
    
    