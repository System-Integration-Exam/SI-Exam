from connection.sqlite_connection import execute_query
from dataclasses import dataclass


@dataclass
class StockInfo:
    uuid: str
    store_id: int
    total_count: int
    reserved_count: int

    def insert_query(self) -> None:
        query = f"INSERT INTO stock_info (uuid, store_id, total_count, reserved_count) VALUES ('{self.uuid}', '{self.store_id}', '{self.total_count}', '{self.reserved_count}')"
        execute_query(query)
