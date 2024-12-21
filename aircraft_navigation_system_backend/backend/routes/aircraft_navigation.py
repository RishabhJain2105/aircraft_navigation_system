from fastapi import APIRouter, HTTPException
from db.database import get_db_connection
from models import AircraftNavigation
from datetime import date

router = APIRouter(prefix="/aircraft-navigation", tags=["Aircraft Navigation"])

@router.get("/", response_model=list[AircraftNavigation])
def get_aircraft_navigation():
    try:
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Aircraft_Navigation")
        result = cursor.fetchall()
        return result
    finally:
        con.close()


@router.get("/maintenance-between-dates", response_model=list[AircraftNavigation])
def get_aircraft_navigation_maintenance_date_range(start_date: date, end_date: date):
    try:
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)

        if start_date > end_date:
            raise HTTPException(status_code=400, detail="Start date cannot be later than end date")

        cursor.execute("""
            SELECT * FROM Aircraft_Navigation
            WHERE last_maintenance_date BETWEEN %s AND %s
        """, (start_date, end_date))

        result = cursor.fetchall()

        if not result:
            raise HTTPException(status_code=404, detail="No aircraft navigation systems found within the given date range")

        return result

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()


@router.get("/installed-between-dates", response_model=list[AircraftNavigation])
def get_aircraft_navigation_installed_date_range(start_date: date, end_date: date):
    try:
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)

        if start_date > end_date:
            raise HTTPException(status_code=400, detail="Start date cannot be later than end date")

        cursor.execute("""
            SELECT * FROM Aircraft_Navigation
            WHERE installed_date BETWEEN %s AND %s
        """, (start_date, end_date))

        result = cursor.fetchall()

        if not result:
            raise HTTPException(status_code=404, detail="No aircraft navigation systems found within the given date range")

        return result

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()


@router.post("/", status_code=201)
def add_aircraft_navigation(nav: AircraftNavigation):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        con.start_transaction()
        if not nav.installed_date or not nav.last_maintenance_date:
            raise HTTPException(status_code=402, detail="Missing input data")
        else:
            cursor.execute(
                "INSERT INTO Aircraft_Navigation (aircraft_id, navigation_system_type, installed_date, last_maintenance_date) "
                "VALUES (%s, %s, %s, %s)",
                (nav.aircraft_id, nav.navigation_system_type, nav.installed_date, nav.last_maintenance_date)
            )
        con.commit()
        return {"message": "Navigation system added successfully"}
    except Exception as e:
        con.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()


@router.put("/{aircraft_id}/{navigation_system_type}", status_code=200)
def update_aircraft_navigation(aircraft_id: int, navigation_system_type: str, nav: AircraftNavigation):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        con.start_transaction()
        if nav.installed_date:
            cursor.execute(
                "UPDATE Aircraft_Navigation SET installed_date = %s, last_maintenance_date = %s "
                "WHERE aircraft_id = %s AND navigation_system_type = %s",
                (nav.installed_date, nav.last_maintenance_date, aircraft_id, navigation_system_type)
            )
        else:
            cursor.execute(
                "UPDATE Aircraft_Navigation SET last_maintenance_date = %s "
                "WHERE aircraft_id = %s AND navigation_system_type = %s",
                (nav.last_maintenance_date, aircraft_id, navigation_system_type)
            )
        if cursor.rowcount == 0:
            con.rollback()
            raise HTTPException(status_code=404, detail="Aircraft Navigation not found or no change made")
        con.commit()
        return {"message": "Aircraft Navigation updated successfully"}
    except Exception as e:
        con.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()


@router.delete("/{aircraft_id}/{navigation_system_type}", status_code=204)
def delete_aircraft_navigation(aircraft_id: int, navigation_system_type: str):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        con.start_transaction()
        cursor.execute(
            "DELETE FROM Aircraft_Navigation WHERE aircraft_id = %s AND navigation_system_type = %s",
            (aircraft_id, navigation_system_type)
        )
        if cursor.rowcount == 0:
            con.rollback()
            raise HTTPException(status_code=404, detail="Aircraft Navigation not found")
        con.commit()
        return {"message": "Aircraft Navigation deleted successfully"}
    except Exception as e:
        con.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()
