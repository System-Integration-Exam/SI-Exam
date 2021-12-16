from connection.sqlite_connection import execute_query
import datetime
from dataclasses import dataclass


@dataclass
class Song:
    title: str
    duration_sec: int
    vinyl_id: str

    def insert_query(self) -> None:
        query = f"INSERT INTO song (title, duration_sec, vinyl_id) VALUES ('{self.title}', '{self.duration_sec}', '{self.vinyl_id}')"
        execute_query(query)
