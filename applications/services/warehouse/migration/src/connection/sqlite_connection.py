import sqlite3

# utils.environment swaps environment variables on import
from utils.config import DATABASE_CONFIG

DATABASE = DATABASE_CONFIG["db"]

def _make_sqlite_connection():
    return sqlite3.connect(f"{DATABASE}.db")



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
        
        