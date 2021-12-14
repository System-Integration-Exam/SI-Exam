import sqlite3

# utils.environment swaps environment variables on import
from utils.config import CONFIG

DATABASE = CONFIG["database"]["name"]

def _make_sqlite_connection():
    return sqlite3.connect(f"./data/{DATABASE}.db")

def execute_query(query):
    conn = _make_sqlite_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def fetch_one(query):
    conn = _make_sqlite_connection()
    cursor = conn.cursor()
    obj = None
    try:
        cursor.execute(query)
        obj = cursor.fetchone()
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return obj

def fetch_all(query):
    
    conn = _make_sqlite_connection()
    cursor = conn.cursor()
    obj_list = None
    try:
        cursor.execute(query)
        obj_list = cursor.fetchall()
        conn.commit()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return obj_list