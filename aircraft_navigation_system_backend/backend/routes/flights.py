from fastapi import APIRouter, HTTPException
from db.database import get_db_connection
from models import Flights

router = APIRouter(prefix="/flights", tags=["Flights"])

@router.get("/", response_model=list[Flights])
def get_flights():
    try:
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Flights")
        result = cursor.fetchall()
        return result
    finally:
        con.close()


@router.get("/departure-arrival-start-end")
def get_departure_arrival_start_end(departure: str, arrival: str, start: str, end:str):
    try:
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM Routes WHERE departure_airport = {departure} AND arrival_airport = {arrival}")

        result = cursor.fetchall()

        if not result:
            raise HTTPException(status_code=404, detail="Route does not exist")

        cursor.execute(
            "SELECT * FROM Flights WHERE route_id = %s AND departure_time BETWEEN %s AND %s",
            (result[0]['route_id'], start+"T00:00:00", end+"T23:59:59")
        )

        result = cursor.fetchall()

        if not result:
            raise HTTPException(status_code=404, detail="No flights found")

        final_result = []
        for flight in result:
            cursor.execute(f"SELECT * FROM Aircraft WHERE aircraft_id = {flight['aircraft_id']}")
            temp_result = cursor.fetchall()[0]
            for aircraft_detail in temp_result:
                flight[aircraft_detail] = temp_result[aircraft_detail]
            final_result.append(flight)
            # print(flight)


        return final_result
    finally:
        con.close()


@router.post("/", status_code=201)
def add_flight(flight: Flights):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        con.start_transaction()
        cursor.execute(
            "INSERT INTO Flights (flight_id, aircraft_id, route_id, departure_time, arrival_time, flight_duration) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (flight.flight_id, flight.aircraft_id, flight.route_id, flight.departure_time, flight.arrival_time, flight.flight_duration)
        )
        con.commit()
        return {"message": "Flight added successfully"}
    except Exception as e:
        con.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()


@router.put("/{flight_id}", status_code=200)
def update_flight(flight_id: int, flight: Flights):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        con.start_transaction()
        cursor.execute(
            "UPDATE Flights SET aircraft_id = %s, route_id = %s, departure_time = %s, arrival_time = %s, flight_duration = %s "
            "WHERE flight_id = %s",
            (flight.aircraft_id, flight.route_id, flight.departure_time, flight.arrival_time, flight.flight_duration, flight_id)
        )
        if cursor.rowcount == 0:
            con.rollback()
            raise HTTPException(status_code=404, detail="Flight not found")
        con.commit()
        return {"message": "Flight updated successfully"}
    except Exception as e:
        con.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()


@router.delete("/{flight_id}", status_code=204)
def delete_flight(flight_id: int):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        con.start_transaction()
        cursor.execute("DELETE FROM Flights WHERE flight_id = %s", (flight_id,))
        if cursor.rowcount == 0:
            con.rollback()
            raise HTTPException(status_code=404, detail="Flight not found")
        con.commit()
        return {"message": "Flight deleted successfully"}
    except Exception as e:
        con.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()
