// // src/components/AircraftNavigation/AddAircraftNavigation.jsx
// import React, { useState, useEffect } from 'react';
// import {
//   Container,
//   Typography,
//   TextField,
//   Button,
//   Box,
//   MenuItem,
//   Snackbar,
//   Alert,
//   CircularProgress,
// } from '@mui/material';
// import { useNavigate } from 'react-router-dom';
// import { getAircraft, addAircraftNavigation } from '../../services/api';

// function AddAircraftNavigation() {
//   const navigate = useNavigate();

//   const [form, setForm] = useState({
//     aircraft_id: '',
//     navigation_system_type: '',
//     installed_date: '',
//     last_maintenance_date: '',
//   });

//   const [aircraftList, setAircraftList] = useState([]);
//   const [loading, setLoading] = useState(true); // Indicates if aircraft data is being fetched
//   const [submitting, setSubmitting] = useState(false); // Indicates if form is being submitted
//   const [alert, setAlert] = useState({ open: false, message: '', severity: 'success' });

//   useEffect(() => {
//     fetchAircraft();
//   }, []);

//   const fetchAircraft = async () => {
//     try {
//       const response = await getAircraft();
//       setAircraftList(response.data);
//       setLoading(false);
//     } catch (error) {
//       console.error('Error fetching Aircraft:', error);
//       setAlert({ open: true, message: 'Failed to fetch Aircraft data.', severity: 'error' });
//       setLoading(false);
//     }
//   };

//   const handleChange = (e) => {
//     setForm({ ...form, [e.target.name]: e.target.value });
//   };

//   const handleSubmit = async (e) => {
//     e.preventDefault();

//     // Basic validation
//     if (
//       !form.aircraft_id ||
//       !form.navigation_system_type ||
//       !form.installed_date ||
//       !form.last_maintenance_date
//     ) {
//       setAlert({ open: true, message: 'All fields are required.', severity: 'warning' });
//       return;
//     }

//     if (new Date(form.installed_date) > new Date(form.last_maintenance_date)) {
//       setAlert({ open: true, message: 'Installed date cannot be after last maintenance date.', severity: 'warning' });
//       return;
//     }

//     setSubmitting(true);

//     try {
//       await addAircraftNavigation(form);
//       setAlert({ open: true, message: 'Navigation system added successfully!', severity: 'success' });
//       setTimeout(() => navigate('/aircraft-navigation'), 1500);
//     } catch (error) {
//       console.error('Error adding Aircraft Navigation:', error);
//       let errorMessage = 'Failed to add navigation system.';
//       if (error.response && error.response.data && error.response.data.detail) {
//         errorMessage = error.response.data.detail;
//       }
//       setAlert({ open: true, message: errorMessage, severity: 'error' });
//       setSubmitting(false);
//     }
//   };

//   const handleCloseAlert = () => {
//     setAlert({ ...alert, open: false });
//   };

//   if (loading) {
//     return (
//       <Container>
//         <Typography variant="h4" gutterBottom>
//           Add Aircraft Navigation System
//         </Typography>
//         <CircularProgress />
//       </Container>
//     );
//   }

//   return (
//     <Container>
//       <Typography variant="h4" gutterBottom>
//         Add Aircraft Navigation System
//       </Typography>
//       <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
//         {/* Aircraft ID Dropdown */}
//         <TextField
//           select
//           label="Aircraft ID"
//           name="aircraft_id"
//           value={form.aircraft_id}
//           onChange={handleChange}
//           fullWidth
//           required
//           margin="normal"
//         >
//           {aircraftList.map((aircraft) => (
//             <MenuItem key={aircraft.aircraft_id} value={aircraft.aircraft_id}>
//               {aircraft.aircraft_id} - {aircraft.model} {/* Adjust based on your Aircraft fields */}
//             </MenuItem>
//           ))}
//         </TextField>

//         {/* Navigation System Type */}
//         <TextField
//           label="Navigation System Type"
//           name="navigation_system_type"
//           value={form.navigation_system_type}
//           onChange={handleChange}
//           fullWidth
//           required
//           margin="normal"
//         />

//         {/* Installed Date */}
//         <TextField
//           label="Installed Date"
//           name="installed_date"
//           type="date"
//           value={form.installed_date}
//           onChange={handleChange}
//           fullWidth
//           required
//           margin="normal"
//           InputLabelProps={{
//             shrink: true,
//           }}
//         />

//         {/* Last Maintenance Date */}
//         <TextField
//           label="Last Maintenance Date"
//           name="last_maintenance_date"
//           type="date"
//           value={form.last_maintenance_date}
//           onChange={handleChange}
//           fullWidth
//           required
//           margin="normal"
//           InputLabelProps={{
//             shrink: true,
//           }}
//         />

//         {/* Submit Button */}
//         <Button
//           type="submit"
//           variant="contained"
//           color="primary"
//           sx={{ mt: 2 }}
//           disabled={submitting}
//         >
//           {submitting ? <CircularProgress size={24} color="inherit" /> : 'Add Navigation System'}
//         </Button>
//       </Box>

//       {/* Snackbar for alerts */}
//       <Snackbar
//         open={alert.open}
//         autoHideDuration={6000}
//         onClose={handleCloseAlert}
//         anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
//       >
//         <Alert onClose={handleCloseAlert} severity={alert.severity} sx={{ width: '100%' }}>
//           {alert.message}
//         </Alert>
//       </Snackbar>
//     </Container>
//   );
// }

// export default AddAircraftNavigation;
