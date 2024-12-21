from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import aircraft_navigation, aircraft, airports, flights, routes, transactions

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(aircraft_navigation.router)
app.include_router(aircraft.router)
app.include_router(airports.router)
app.include_router(routes.router)
app.include_router(flights.router)
app.include_router(transactions.router)

# uvicorn main:app --reload
 