// src/pages/Flights/EditFlight.jsx
import React, { useState, useEffect } from 'react';
import {
  Container,
  Typography,
  TextField,
  Button,
  Box,
  MenuItem,
  Snackbar,
  Alert,
} from '@mui/material';
import { useNavigate } from 'react-router-dom';
import { getFlights, updateFlight, getAircraft, getRoutes } from '../../services/api';

function EditFlight() {
  const [flights, setFlights] = useState([]);
  const [form, setForm] = useState({
    flight_id: '',
    aircraft_id: '',
    route_id: '',
    departure_time: '',
    arrival_time: '',
    flight_duration: '',
  });
  const [aircraftOptions, setAircraftOptions] = useState([]);
  const [routeOptions, setRouteOptions] = useState([]);
  const [alert, setAlert] = useState({ open: false, message: '', severity: 'success' });

  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [flightsRes, aircraftRes, routesRes] = await Promise.all([
          getFlights(),
          getAircraft(),
          getRoutes(),
        ]);
        setFlights(flightsRes.data.filter((flight) => flight.status === 'Scheduled')); // Filter scheduled flights
        setAircraftOptions(aircraftRes.data);
        setRouteOptions(routesRes.data);
      } catch (error) {
        console.error('Error fetching data:', error);
        setAlert({ open: true, message: 'Failed to fetch data.', severity: 'error' });
      }
    };
    fetchData();
  }, []);

  const handleFlightSelect = (e) => {
    const selectedFlight = flights.find((flight) => flight.flight_id === parseInt(e.target.value));
    if (selectedFlight) {
      setForm({
        flight_id: selectedFlight.flight_id,
        aircraft_id: selectedFlight.aircraft_id,
        route_id: selectedFlight.route_id,
        departure_time: selectedFlight.departure_time,
        arrival_time: selectedFlight.arrival_time,
        flight_duration: selectedFlight.flight_duration,
      });
    }
  };

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!form.flight_id) {
      setAlert({ open: true, message: 'Please select a flight to edit.', severity: 'warning' });
      return;
    }

    // Calculate flight duration in hours
    const departure = new Date(form.departure_time);
    const arrival = new Date(form.arrival_time);
    const duration = (arrival - departure) / (1000 * 60 * 60); // duration in hours

    if (duration <= 0) {
      setAlert({ open: true, message: 'Arrival time must be after departure time.', severity: 'warning' });
      return;
    }

    const updatedData = {
      aircraft_id: form.aircraft_id,
      route_id: form.route_id,
      departure_time: form.departure_time,
      arrival_time: form.arrival_time,
      flight_duration: duration,
    };

    try {
      await updateFlight(form.flight_id, updatedData);
      setAlert({ open: true, message: 'Flight updated successfully!', severity: 'success' });
      setTimeout(() => navigate('/flights'), 1500);
    } catch (error) {
      console.error('Error updating flight:', error);
      setAlert({ open: true, message: 'Failed to update flight.', severity: 'error' });
    }
  };

  const handleCloseAlert = () => {
    setAlert({ ...alert, open: false });
  };

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Edit Flight
      </Typography>
      <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
        <TextField
          select
          label="Select Scheduled Flight"
          name="flight_id"
          value={form.flight_id}
          onChange={handleFlightSelect}
          fullWidth
          required
          margin="normal"
        >
          {flights.map((flight) => (
            <MenuItem key={flight.flight_id} value={flight.flight_id}>
              Flight {flight.flight_id}: Aircraft {flight.aircraft_id} | Route {flight.route_id}
            </MenuItem>
          ))}
        </TextField>

        <TextField
          select
          label="Aircraft"
          name="aircraft_id"
          value={form.aircraft_id}
          onChange={handleChange}
          fullWidth
          required
          margin="normal"
        >
          {aircraftOptions.map((aircraft) => (
            <MenuItem key={aircraft.aircraft_id} value={aircraft.aircraft_id}>
              {aircraft.model} ({aircraft.airline_name})
            </MenuItem>
          ))}
        </TextField>

        <TextField
          select
          label="Route"
          name="route_id"
          value={form.route_id}
          onChange={handleChange}
          fullWidth
          required
          margin="normal"
        >
          {routeOptions.map((route) => (
            <MenuItem key={route.route_id} value={route.route_id}>
              Route {route.route_id}: {route.departure_airport} to {route.arrival_airport}
            </MenuItem>
          ))}
        </TextField>

        <TextField
          label="Departure Time"
          name="departure_time"
          type="datetime-local"
          value={form.departure_time}
          onChange={handleChange}
          fullWidth
          required
          margin="normal"
          InputLabelProps={{
            shrink: true,
          }}
        />

        <TextField
          label="Arrival Time"
          name="arrival_time"
          type="datetime-local"
          value={form.arrival_time}
          onChange={handleChange}
          fullWidth
          required
          margin="normal"
          InputLabelProps={{
            shrink: true,
          }}
        />

        <Button type="submit" variant="contained" color="primary" sx={{ mt: 2 }}>
          Update Flight
        </Button>
      </Box>

      {/* Snackbar for alerts */}
      <Snackbar
        open={alert.open}
        autoHideDuration={6000}
        onClose={handleCloseAlert}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      >
        <Alert onClose={handleCloseAlert} severity={alert.severity} sx={{ width: '100%' }}>
          {alert.message}
        </Alert>
      </Snackbar>
    </Container>
  );
}

export default EditFlight;
