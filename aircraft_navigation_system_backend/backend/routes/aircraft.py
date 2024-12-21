from fastapi import APIRouter, HTTPException
from db.database import get_db_connection
from models import Aircraft

router = APIRouter(prefix="/aircraft", tags=["Aircraft"])

@router.get("/", response_model=list[Aircraft])
def get_aircraft():
    try:
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Aircraft")
        result = cursor.fetchall()
        return result
    finally:
        con.close()


@router.post("/", status_code=201)
def add_aircraft(aircraft: Aircraft):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        con.start_transaction()
        cursor.execute(
            "INSERT INTO Aircraft (aircraft_id, model, manufacturer, capacity, `range`, airline_name) "
            "VALUES (%s, %s, %s, %s, %s, %s)",
            (aircraft.aircraft_id, aircraft.model, aircraft.manufacturer, aircraft.capacity, aircraft.range, aircraft.airline_name)
        )
        con.commit()
        return {"message": "Aircraft added successfully"}
    except Exception as e:
        con.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()


@router.put("/{aircraft_id}", status_code=200)
def update_aircraft(aircraft_id: int, aircraft: Aircraft):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        con.start_transaction()
        cursor.execute(
            "UPDATE Aircraft SET model = %s, manufacturer = %s, capacity = %s, `range` = %s, airline_name = %s "
            "WHERE aircraft_id = %s",
            (aircraft.model, aircraft.manufacturer, aircraft.capacity, aircraft.range, aircraft.airline_name, aircraft_id)
        )
        if cursor.rowcount == 0:
            con.rollback()
            raise HTTPException(status_code=404, detail="Aircraft not found")
        con.commit()
        return {"message": "Aircraft updated successfully"}
    except Exception as e:
        con.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()
        

@router.delete("/{aircraft_id}", status_code=204)
def delete_aircraft(aircraft_id: int):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        con.start_transaction()
        cursor.execute("DELETE FROM Aircraft WHERE aircraft_id = %s", (aircraft_id,))
        if cursor.rowcount == 0:
            con.rollback()
            raise HTTPException(status_code=404, detail="Aircraft not found")
        con.commit()
        return {"message": "Aircraft deleted successfully"}
    except Exception as e:
        con.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()
