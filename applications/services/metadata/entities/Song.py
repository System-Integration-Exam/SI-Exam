from dataclasses import dataclass


@dataclass
class Song:
    """Class for book-metadata"""

    id: str
    title: str
    duration_sec: int
    vinyl_id: str

    def __init__(self, id: str, title: str, duration_sec: int, vinyl_id: str):
        self.id = id
        self.title = title
        self.duration_sec = duration_sec
        self.vinyl_id = vinyl_id
