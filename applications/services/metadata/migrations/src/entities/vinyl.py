from connection.sqlite_connection import execute_query
import datetime
from dataclasses import dataclass

@dataclass
class Vinyl():
    id: str
    artist: str
    genre: str

    def insert_query(self) -> None:
        query = f"INSERT INTO store (id, artist, genre) VALUES ('{self.id}', '{self.artist}', '{self.genre}')"
        execute_query(query)