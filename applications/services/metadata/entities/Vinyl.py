from dataclasses import dataclass


@dataclass
class Vinyl:
    """Class for book-metadata"""

    id: str
    artist: str
    genre: str

    def __init__(self, id: str, artist: str, genre: str):
        self.id = id
        self.artist = artist
        self.genre = genre
