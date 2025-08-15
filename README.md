# Aircraft Navigation System

Welcome to the Aircraft Navigation System - a comprehensive full-stack application designed to manage and monitor aircraft operations, navigation systems, flight routes, and airport data. This system combines the power of FastAPI for the backend with a modern React frontend to deliver a seamless aviation management experience.

## What This System Does

This Aircraft Navigation System is your all-in-one solution for:

- **Aircraft Management**: Track and manage your fleet with detailed aircraft information including models, manufacturers, capacity, and range specifications
- **Navigation System Monitoring**: Keep tabs on GPS, Autopilot, and Radar systems with installation dates and maintenance schedules  
- **Airport Database**: Maintain comprehensive airport information with IATA codes, geographical coordinates, and location details
- **Route Planning**: Define and manage flight routes with waypoints and distance calculations
- **Flight Operations**: Schedule and track flights with departure/arrival times and duration management
- **Real-time Search**: Quickly find flights by airline, aircraft by model, routes by airports, and more

## System Architecture

The system is built with a modern tech stack:

**Backend (FastAPI + MySQL)**
- FastAPI framework for high-performance API development
- MySQL database for reliable data storage
- Pydantic models for data validation
- CORS middleware for frontend integration

**Frontend (React + Vite + Material-UI)**  
- React 18 with modern hooks and components
- Vite for lightning-fast development and building
- Material-UI for beautiful, responsive design
- Axios for seamless API communication
- React Router for smooth navigation

## Project Structure

```
aircraft_navigation_system/
├── aircraft_navigation_system_backend/
│   └── backend/
│       ├── db/                     # Database configurations and schemas
│       │   ├── database.py         # Database connection handler
│       │   ├── schema.sql          # Database schema definition
│       │   └── initializer.py      # Database initialization
│       ├── routes/                 # API route handlers
│       │   ├── aircraft.py         # Aircraft management endpoints
│       │   ├── aircraft_navigation.py # Navigation system endpoints  
│       │   ├── airports.py         # Airport management endpoints
│       │   ├── flights.py          # Flight operations endpoints
│       │   ├── routes.py           # Route management endpoints
│       │   └── transactions.py     # Transaction handling
│       ├── models.py               # Pydantic data models
│       ├── main.py                 # FastAPI application entry point
│       └── requirements.txt        # Python dependencies
├── airline-front-end/
│   ├── src/
│   │   ├── components/             # Reusable React components  
│   │   ├── pages/                  # Page components for different features
│   │   ├── services/               # API service functions
│   │   ├── App.jsx                 # Main React application
│   │   └── main.jsx               # React entry point
│   ├── package.json               # Node.js dependencies
│   └── vite.config.js             # Vite configuration
```

## Getting Started

### Prerequisites

Before diving in, make sure you have these installed on your system:

- **Python 3.8+** - The backbone of our backend
- **Node.js 16+** - Powers our React frontend  
- **npm or yarn** - Package manager for JavaScript dependencies
- **MySQL** - Our reliable database system

### Database Setup

1. **Install and start MySQL** on your system
2. **Create a new database** for the project:
   ```sql
   CREATE DATABASE aircraft_navigation_db;
   ```
3. **Update database connection** in `backend/db/database.py` with your MySQL credentials

### Backend Installation & Setup

1. **Navigate to the backend directory:**
   ```bash
   cd aircraft_navigation_system_backend/backend
   ```

2. **Create a Python virtual environment** (highly recommended):
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database** by running the schema:
   ```bash
   python initializer.py
   ```

5. **Start the FastAPI development server:**
   ```bash
   uvicorn main:app --reload
   ```

   Your API will be running at `http://localhost:8000` 

   **Pro tip**: Visit `http://localhost:8000/docs` to explore the interactive API documentation!

### Frontend Installation & Setup

1. **Navigate to the frontend directory:**
   ```bash
   cd airline-front-end
   ```

2. **Install Node.js dependencies:**
   ```bash
   npm install
   # or if you prefer yarn:
   yarn install
   ```

3. **Start the React development server:**
   ```bash
   npm run dev
   # or with yarn:
   yarn dev
   ```

   Your frontend will be running at `http://localhost:5173` 

## How to Use the System

### Accessing the Application
1. **Start both servers** (backend on port 8000, frontend on port 5173)
2. **Open your browser** and navigate to `http://localhost:5173`
3. **Explore the dashboard** to access different modules

### Key Features You Can Use:

** Aircraft Management**
- Add new aircraft with specifications
- View your complete fleet inventory  
- Update aircraft details and maintenance records
- Track aircraft by manufacturer and model

** Navigation Systems**
- Monitor GPS, Autopilot, and Radar systems
- Schedule and track maintenance dates
- Filter systems by installation or maintenance periods

** Airport Operations**  
- Maintain comprehensive airport database
- Search airports by name, city, or country
- Manage IATA codes and geographical coordinates

** Route Planning**
- Create flight routes between airports
- Define waypoints and calculate distances  
- Manage departure and arrival airports

** Flight Operations**
- Schedule flights with aircraft and route assignments
- Track departure and arrival times
- Monitor flight durations and status

## Configuration Notes

### Database Connection
Update the database credentials in `backend/db/database.py`:
```python
config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password', 
    'database': 'aircraft_navigation_db'
}
```

### API Base URL
The frontend is configured to connect to the backend at `http://127.0.0.1:8000`. If you need to change this, update the `API_BASE_URL` in `airline-front-end/src/services/api.js`.

## Development Commands

### Backend Commands
```bash
# Start development server with auto-reload
uvicorn main:app --reload

# Start on different port
uvicorn main:app --reload --port 8080

# Run with specific host
uvicorn main:app --reload --host 0.0.0.0
```

### Frontend Commands
```bash
# Start development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview

# Run linting
npm run lint
```

## API Endpoints Overview

The system provides comprehensive REST API endpoints:

- **Aircraft**: `/aircraft` - CRUD operations for aircraft management
- **Navigation**: `/aircraft-navigation` - Navigation system tracking
- **Airports**: `/airports` - Airport database management  
- **Routes**: `/routes` - Flight route planning
- **Flights**: `/flights` - Flight operations management
- **Transactions**: `/transactions` - Transaction handling

---
