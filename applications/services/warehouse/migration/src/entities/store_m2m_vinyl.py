from connection.sqlite_connection import execute_query
import datetime
from dataclass import dataclass

@dataclass
class StoreM2MVinyl():
    store_id: int
    vinyl_id: int

    def insert_query(self) -> None:
        query = f"INSERT INTO store_m2m_vinyl (store_id, vinyl_id) VALUES ('{self.address}', '{self.phone_number}')"
        execute_query(query)