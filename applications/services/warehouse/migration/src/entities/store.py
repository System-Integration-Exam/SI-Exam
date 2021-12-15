from connection.sqlite_connection import execute_query
import datetime
from dataclasses import dataclass


@dataclass
class Store:
    address: str
    phone_number: str
    email: str
    # created_at: datetime.date
    # updated_at: datetime.date

    def insert_query(self) -> None:
        query = f"INSERT INTO store (address, phone_number, email) VALUES ('{self.address}', '{self.phone_number}', '{self.email}')"
        execute_query(query)
