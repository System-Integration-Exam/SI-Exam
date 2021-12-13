from dataclasses import dataclass

@dataclass
class Song:
    """Class for book-metadata"""
    id: str
    title: str
    duration_sec: int

    def __init__(self, id: str, title: str, duration_sec: int):
        self.id = id
        self.title = title
        self.duration_sec = duration_sec

