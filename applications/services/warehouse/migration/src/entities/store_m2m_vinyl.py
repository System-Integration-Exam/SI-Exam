from connection.sqlite_connection import execute_query
import datetime
from dataclasses import dataclass

@dataclass
class StoreM2MVinyl():
    store_id: int
    vinyl_id: int

    def insert_query(self) -> None:
        query = f"INSERT INTO store_m2m_vinyl (store_id, vinyl_id) VALUES ('{self.store_id}', '{self.vinyl_id}')"
        execute_query(query)