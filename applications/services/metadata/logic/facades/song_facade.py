import sqlite3
from entities.Song import Song


def createSong(song):
    conn = sqlite3.connect("./data/metadata.db")
    c = conn.cursor()
    try:
        song = c.execute(
            """
            INSERT INTO song (title, duration_sec, vinyl_id)
            VALUES (:title, :duration_sec, :vinyl_id)
            RETURNING *
            """,
            {
                "title": song.title,
                "duration_sec": song.duration_sec,
                "vinyl_id": song.vinyl_id,
            },
        ).fetchall()[::-1][0]
        conn.commit()
        return song
    finally:
        c.close()
        conn.close()


def getSongById(id):
    conn = sqlite3.connect("./data/metadata.db")
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM song WHERE id = :id", {"id": id})
        row = c.fetchone()
        song = Song(row[0], row[1], row[2], row[3])
        return song
    finally:
        c.close()
        conn.close()


def updateSong(song):
    conn = sqlite3.connect("./data/metadata.db")
    c = conn.cursor()
    try:
        c.execute(
            "UPDATE song SET title = :title, duration_sec = :duration_sec, vinyl_id = :vinyl_id WHERE id = :id",
            {
                "id": song.id,
                "title": song.title,
                "duration_sec": song.duration_sec,
                "vinyl_id": song.vinyl_id,
            },
        )
        conn.commit()
        statusMessage = "Song successfully updated."
        return statusMessage
    finally:
        c.close()
        conn.close()


def deleteSongById(id):
    conn = sqlite3.connect("./data/metadata.db")
    c = conn.cursor()
    try:
        c.execute("DELETE FROM song WHERE id = :id", {"id": id})
        conn.commit()
        statusMessage = "Song with given ID has been removed."
        return statusMessage
    finally:
        c.close()
        conn.close()


def getAllSongs():
    conn = sqlite3.connect("./data/metadata.db")
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM song")
        row = c.fetchall()
        result = []
        for x in row:
            song = Song(x[0], x[1], x[2], x[3])
            result.append(song)
        return result
    finally:
        c.close()
        conn.close()
