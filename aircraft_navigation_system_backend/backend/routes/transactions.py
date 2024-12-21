from fastapi import APIRouter, HTTPException
from db.database import get_db_connection
import os

router = APIRouter(prefix="/transactions", tags=["Transactions"])

SAVEPOINTS_FILE = "savepoints.txt"
MAX_SAVEPOINTS = 100

def load_savepoints():
    """Load savepoints from the file."""
    if not os.path.exists(SAVEPOINTS_FILE):
        return []
    with open(SAVEPOINTS_FILE, "r") as f:
        lines = f.readlines()
    return [line.strip().split(",") for line in lines]


def save_savepoints(savepoints):
    """Save savepoints to the file, limiting to MAX_SAVEPOINTS."""
    with open(SAVEPOINTS_FILE, "w") as f:
        for connection_id, savepoint_name in savepoints[-MAX_SAVEPOINTS:]:
            f.write(f"{connection_id},{savepoint_name}\n")


def add_savepoint_to_file(connection_id, savepoint_name):
    """Add a new savepoint to the file."""
    savepoints = load_savepoints()
    savepoints.append((connection_id, savepoint_name))
    save_savepoints(savepoints)


def get_savepoints_from_file(connection_id):
    """Get savepoints for a specific connection."""
    savepoints = load_savepoints()
    return [name for cid, name in savepoints if cid == connection_id]


@router.post("/savepoint/{name}")
def create_savepoint(name: str):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        con_id = str(id(con))
        cursor.execute(f"SAVEPOINT {name}")
        add_savepoint_to_file(con_id, name)
        return {"message": f"Savepoint '{name}' created successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()


@router.get("/savepoints")
def list_savepoints():
    try:
        con = get_db_connection()
        con_id = str(id(con))
        available_savepoints = get_savepoints_from_file(con_id)
        print(available_savepoints)
        if not available_savepoints:
            return {"savepoints": [], "message": "No savepoints available"}
        return {"savepoints": available_savepoints}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()


@router.post("/rollback/{name}")
def rollback_to_savepoint(name: str):
    try:
        con = get_db_connection()
        cursor = con.cursor()
        con_id = str(id(con))
        available_savepoints = get_savepoints_from_file(con_id)
        if name not in available_savepoints:
            raise HTTPException(status_code=404, detail=f"Savepoint '{name}' not found")
        cursor.execute(f"ROLLBACK TO SAVEPOINT {name}")
        return {"message": f"Rolled back to savepoint '{name}' successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        con.close()
