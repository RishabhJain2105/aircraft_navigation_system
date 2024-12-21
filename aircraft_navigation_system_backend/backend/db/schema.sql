CREATE TABLE IF NOT EXISTS Aircraft (
    aircraft_id INT PRIMARY KEY CHECK (aircraft_id > 0),
    model VARCHAR(100) NOT NULL,
    manufacturer VARCHAR(100) NOT NULL,
    capacity INT NOT NULL CHECK (capacity > 0),
    `range` INT NOT NULL CHECK (`range` > 0),
    airline_name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS Aircraft_Navigation (
    aircraft_id INT NOT NULL,
    navigation_system_type VARCHAR(100) NOT NULL,
    installed_date DATE NOT NULL,
    last_maintenance_date DATE,
    PRIMARY KEY (aircraft_id, navigation_system_type),
    FOREIGN KEY (aircraft_id) REFERENCES Aircraft(aircraft_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Airports (
    airport_id INT PRIMARY KEY CHECK (airport_id > 0),
    airport_name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    IATA_code VARCHAR(3) NOT NULL,
    latitude FLOAT NOT NULL CHECK (latitude BETWEEN -90 AND 90),
    longitude FLOAT NOT NULL CHECK (longitude BETWEEN -180 AND 180)
);

CREATE TABLE IF NOT EXISTS Routes (
    route_id INT PRIMARY KEY CHECK (route_id > 0),
    departure_airport INT NOT NULL,
    arrival_airport INT NOT NULL,
    waypoints TEXT,
    distance FLOAT NOT NULL CHECK (distance > 0),
    FOREIGN KEY (departure_airport) REFERENCES Airports(airport_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (arrival_airport) REFERENCES Airports(airport_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Flights (
    flight_id INT PRIMARY KEY CHECK (flight_id > 0),
    aircraft_id INT NOT NULL,
    route_id INT NOT NULL,
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL,
    flight_duration FLOAT,
    FOREIGN KEY (aircraft_id) REFERENCES Aircraft(aircraft_id) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (route_id) REFERENCES Routes(route_id) ON DELETE CASCADE ON UPDATE CASCADE
);