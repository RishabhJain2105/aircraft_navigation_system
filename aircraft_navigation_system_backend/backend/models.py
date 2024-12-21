from pydantic import BaseModel
from datetime import date, datetime
from typing import Union, Optional

class Aircraft(BaseModel):
    aircraft_id: int
    model: str
    manufacturer: str
    capacity: int
    range: int
    airline_name: str

class AircraftNavigation(BaseModel):
    aircraft_id: int
    # GPS / Autopilot / Radar
    navigation_system_type: str
    # YYYY-MM-DD
    installed_date: Optional[Union[str, date]] = None
    # YYYY-MM-DD
    last_maintenance_date: Optional[Union[str, date]] = None

class Airports(BaseModel):
    airport_id: Optional[int] = None
    airport_name: str
    city: str
    country: str
    IATA_code: str
    latitude: float
    longitude: float

class Routes(BaseModel):
    route_id: Optional[int] = None
    departure_airport: int
    arrival_airport: int
    waypoints: str
    distance: float

class Flights(BaseModel):
    flight_id: int
    aircraft_id: int
    route_id: int
    # YYYY-MM-DD HH:MM:SS
    departure_time: datetime
    # YYYY-MM-DD HH:MM:SS
    arrival_time: datetime
    flight_duration: float
