from connection.sqlite_connection import execute_query
from dataclasses import dataclass

@dataclass
class Customer():
    first_name: str
    last_name: str
    email: str
    phone_number: str

    def insert_query(self) -> None:
        query = f"INSERT INTO customer (first_name, last_name, email, phone_number) VALUES ('{self.first_name}', '{self.last_name}', '{self.email}', '{self.phone_number}')"
        execute_query(query)