import sqlite3
from sqlite3 import Error
from utils.config import ROOT_DIR
import os


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("sqllite3 version: " + sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    path = os.path.dirname(ROOT_DIR) + "/data/metadata.db"
    create_connection(f"{path}") 