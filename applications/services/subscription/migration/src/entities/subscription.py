from connection.sqlite_connection import execute_query
import datetime
from dataclasses import dataclass


@dataclass
class Subscription:
    is_active: bool
    expiration_date: datetime.datetime

    def insert_query(self) -> None:
        query = f"INSERT INTO subscription (is_active, expiration_date) VALUES ({self.is_active}, '{self.expiration_date}')"
        execute_query(query)
