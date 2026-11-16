# Aircraft management project in Django

A Django project with 14 models and a REST API (Django REST Framework).

## Tech stack

- Python 3
- Django
- Django REST Framework
- django-cors-headers
- psycopg2 (PostgreSQL)
- Pillow
- Database: PostgreSQL

## Project structure

- `aircraft_mgt_project/aircraft_mgt_project/`: project settings and root URLs
- `aircraft_mgt_project/aircraft_app/`: Django app
- Tests: `aircraft_mgt_project/aircraft_app/tests.py`

## Data model

| Model | App | Fields |
|---|---|---|
| `Aircraft` | `aircraft_mgt_project/aircraft_app` | registration_number, name, model, aircraft_type, price, description, image, manufacturing_date, fuel_capacity, max_speed … |
| `Sensor` | `aircraft_mgt_project/aircraft_app` | name, sensor_type, anufacturer, model_number, serial_number, min_value, max_value, unit, accuracy, status … |
| `Communication` | `aircraft_mgt_project/aircraft_app` | communication_type, sender, receiver, message_content, flight_phase, altitude, latitude, longitude, frequency, signal_strength … |
| `Flight` | `aircraft_mgt_project/aircraft_app` | flight_number, departure_airport, arrival_airport, departure_time, arrival_time, duration_hours, distance_km, altitude_max, status, aircraft |
| `Certification` | `aircraft_mgt_project/aircraft_app` | name, issuing_authority, valid_from, valid_until |
| `CrewMember` | `aircraft_mgt_project/aircraft_app` | employee_id, role, hire_date, certifications, total_flight_hours, phone_number, emergency_contact, emergency_phone, is_active, user … |
| `AircraftCommunication` | `aircraft_mgt_project/aircraft_app` | aircraft, communication, duration, satart_date_time |
| `FlightCrewMember` | `aircraft_mgt_project/aircraft_app` | flight, crew_member, role, assigned_at |
| `Airport` | `aircraft_mgt_project/aircraft_app` | iata_code, icao_code, name, city, country, latitude, longitude |
| `Route` | `aircraft_mgt_project/aircraft_app` | origin, destination, distance_km, is_international |
| `FlightPlan` | `aircraft_mgt_project/aircraft_app` | flight, route, filed_time, alternate_airport, cruising_altitude_ft, fuel_required_kg, remarks |
| `WeatherReport` | `aircraft_mgt_project/aircraft_app` | airport, timestamp, temperature_c, wind_speed_kt, visibility_km, metar |
| `MaintenanceTask` | `aircraft_mgt_project/aircraft_app` | code, title, description, estimated_hours, category |
| `MaintenanceRecord` | `aircraft_mgt_project/aircraft_app` | aircraft, work_order_number, status, priority |

## URL routes

Declared in `urls.py`:

- `/aircraft/ (router)`
- `/Flight/ (router)`
- `/Crew-member/ (router)`
- `/flight-crew-member/ (router)`
- `/blog/`
- `/api/`

## How to run

```bash
cd aircraft_mgt_project
pip install pipenv
pipenv install
pipenv shell
python manage.py migrate
python manage.py runserver
```

`settings.py` is configured for PostgreSQL: create the database and use your own credentials before running `migrate`.

Then open `http://127.0.0.1:8000/`.

---

Author: [Chaouki Bayoudhi](https://github.com/ChaoukiBayoudhi)
