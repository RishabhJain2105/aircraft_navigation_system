// src/components/AircraftNavigation/AircraftNavigationList.jsx
import React, { useState, useEffect } from 'react';
import {
  Container,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  CircularProgress,
} from '@mui/material';
import { getAircraftNavigation } from '../../services/api';

function AircraftNavigationList() {
  const [navigationData, setNavigationData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchAircraftNavigation();
  }, []);

  const fetchAircraftNavigation = async () => {
    try {
      const response = await getAircraftNavigation();
      setNavigationData(response.data);
    } catch (error) {
      console.error('Error fetching Aircraft Navigation:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <Container>
        <Typography variant="h4" gutterBottom>
          Aircraft Navigation Systems
        </Typography>
        <CircularProgress />
      </Container>
    );
  }

  return (
    <Container>
      <Typography variant="h4" gutterBottom>
        Aircraft Navigation Systems
      </Typography>
      {navigationData.length === 0 ? (
        <Typography>No Aircraft Navigation Systems available.</Typography>
      ) : (
        <TableContainer component={Paper}>
          <Table aria-label="Aircraft Navigation Table">
            <TableHead>
              <TableRow>
                <TableCell>Aircraft ID</TableCell>
                <TableCell>Navigation System Type</TableCell>
                <TableCell>Installed Date</TableCell>
                <TableCell>Last Maintenance Date</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {navigationData.map((nav) => (
                <TableRow key={nav.aircraft_id}>
                  <TableCell>{nav.aircraft_id}</TableCell>
                  <TableCell>{nav.navigation_system_type}</TableCell>
                  <TableCell>{nav.installed_date ? new Date(nav.installed_date).toLocaleDateString() : 'N/A'}</TableCell>
                  <TableCell>{nav.last_maintenance_date ? new Date(nav.last_maintenance_date).toLocaleDateString() : 'N/A'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </Container>
  );
}

export default AircraftNavigationList;
