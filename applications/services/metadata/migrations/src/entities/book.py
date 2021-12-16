from connection.sqlite_connection import execute_query
from dataclasses import dataclass

@dataclass
class Book():
    title: str
    author: str
    rating: int

    def insert_query(self) -> None:
        query = f"INSERT INTO Book (title, author, rating) VALUES ('{self.title}','{self.author}','{self.rating}')"
        execute_query(query)