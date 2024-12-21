from fastapi import APIRouter, HTTPException
from db.database import get_db_connection
from models import Routes

router = APIRouter(prefix="/routes", tags=["Routes"])

@router.get("/", response_model=list[Routes])
def get_routes():
    try:
        con = get_db_connection()
        cursor = con.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Routes")
        result = cursor.fetchall()
        return result
    finally:
        con.close()


@router.post("/", status_code=201)
def add_route(route: Routes):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        # Start a transaction
        con.start_transaction()
        cursor.execute("SELECT route_id FROM Routes")
        result = cursor.fetchall()
        start = 1
        # print(result)
        for id in result:
            if id[0] != start:
                break
            start += 1
        route.route_id = start
        cursor.execute(
            "INSERT INTO Routes (route_id, departure_airport, arrival_airport, waypoints, distance) "
            "VALUES (%s, %s, %s, %s, %s)",
            (route.route_id, route.departure_airport, route.arrival_airport, route.waypoints, route.distance)
        )

        # Commit the transaction
        con.commit()
        return {"message": "Route added successfully"}
    except Exception as e:
        # Rollback the transaction if an error occurs
        con.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()


@router.put("/{route_id}", status_code=200)
def update_route(route_id: int, route: Routes):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        # Start a transaction
        con.start_transaction()

        cursor.execute(
            "UPDATE Routes SET departure_airport = %s, arrival_airport = %s, waypoints = %s, distance = %s "
            "WHERE route_id = %s",
            (route.departure_airport, route.arrival_airport, route.waypoints, route.distance, route_id)
        )
        if cursor.rowcount == 0:
            con.rollback()
            raise HTTPException(status_code=404, detail="Route not found")

        # Commit the transaction
        con.commit()
        return {"message": "Route updated successfully"}
    except Exception as e:
        # Rollback the transaction if an error occurs
        con.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()


@router.delete("/{route_id}", status_code=204)
def delete_route(route_id: int):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        # Start a transaction
        con.start_transaction()

        cursor.execute("DELETE FROM Routes WHERE route_id = %s", (route_id,))
        if cursor.rowcount == 0:
            con.rollback()
            raise HTTPException(status_code=404, detail="Route not found")

        # Commit the transaction
        con.commit()
        return {"message": "Route deleted successfully"}
    except Exception as e:
        # Rollback the transaction if an error occurs
        con.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()
