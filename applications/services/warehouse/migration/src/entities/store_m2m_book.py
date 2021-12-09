from connection.sqlite_connection import execute_query
import datetime
from dataclasses import dataclass

@dataclass
class StoreM2MBook():
    store_id: int
    book_id: int

    def insert_query(self) -> None:
        query = f"INSERT INTO store_m2m_book (store_id, book_id) VALUES ('{self.store_id}', '{self.book_id}')"
        execute_query(query)