
from dataclasses import dataclass

@dataclass
class Book:
    """Class for book-metadata"""
    id: int
    title: str
    author: str
    rating: int

    def __init__(self, id: int, title: str, author: str, rating: int):
        self.id = id
        self.title = title
        self.author = author
        self.rating = rating

    def create():
        return 0

    def read():
        return 0

    def update():
        return 0
    
    def delete():
        return 0

