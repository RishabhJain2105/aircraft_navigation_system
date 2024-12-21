from fastapi import APIRouter, HTTPException
from db.database import get_db_connection
from models import Airports

router = APIRouter(prefix="/airports", tags=["Airports"])

@router.get("/", response_model=list[Airports])
def get_airports():
    try:
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Airports")
        result = cursor.fetchall()
        return result
    finally:
        con.close()


@router.post("/", status_code=201)
def add_airport(airport: Airports):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        con.start_transaction()
        cursor.execute("SELECT airport_id FROM Airports")
        result = cursor.fetchall()
        start = 1
        # print(result)
        for id in result:
            if id[0] != start:
                break
            start += 1
        airport.airport_id = start
        # print(airport)
        cursor.execute(
            "INSERT INTO Airports (airport_id, airport_name, city, country, IATA_code, latitude, longitude) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (airport.airport_id, airport.airport_name, airport.city, airport.country, airport.IATA_code, airport.latitude, airport.longitude)
        )
        con.commit()
        return {"message": "Airport added successfully"}
    except Exception as e:
        con.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()


@router.put("/{airport_id}", status_code=200)
def update_airport(airport_id: int, airport: Airports):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        con.start_transaction()
        cursor.execute(
            "UPDATE Airports SET airport_name = %s, city = %s, country = %s, IATA_code = %s, latitude = %s, longitude = %s "
            "WHERE airport_id = %s",
            (airport.airport_name, airport.city, airport.country, airport.IATA_code, airport.latitude, airport.longitude, airport_id)
        )
        if cursor.rowcount == 0:
            con.rollback()
            raise HTTPException(status_code=404, detail="Airport not found")
        con.commit()
        return {"message": "Airport updated successfully"}
    except Exception as e:
        con.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()


@router.delete("/{airport_id}", status_code=204)
def delete_airport(airport_id: int):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        con.start_transaction()
        cursor.execute("DELETE FROM Airports WHERE airport_id = %s", (airport_id,))
        if cursor.rowcount == 0:
            con.rollback()
            raise HTTPException(status_code=404, detail="Airport not found")
        con.commit()
        return {"message": "Airport deleted successfully"}
    except Exception as e:
        con.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()
