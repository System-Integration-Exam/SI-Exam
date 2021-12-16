import sqlite3
from entities.Vinyl import Vinyl


def createVinyl(vinyl):
    conn = sqlite3.connect("./data/metadata.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO vinyl (artist, genre) VALUES (:artist, :genre)", {'artist': vinyl.artist, 'genre': vinyl.genre})
        conn.commit()
        statusMessage = "Vinyl successfully created."
        return statusMessage
    finally:
        c.close()
        conn.close()


def getVinylById(id):
    conn = sqlite3.connect("./data/metadata.db")
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM vinyl WHERE id = :id", {'id': id})
        row = c.fetchone()
        vinyl = Vinyl(row[0], row[1], row[2])
        return vinyl
    finally:
        c.close()
        conn.close()


def updateVinyl(vinyl):
    conn = sqlite3.connect("./data/metadata.db")
    c = conn.cursor()
    try:
        c.execute("UPDATE vinyl SET artist = :artist, genre = :genre WHERE id = :id", {'id': vinyl.id, 'artist': vinyl.artist, 'genre': vinyl.genre})
        conn.commit()
        statusMessage = "Vinyl successfully created."
        return statusMessage
    finally:
        c.close()
        conn.close()
    

def deleteVinylById(id):
    conn = sqlite3.connect("./data/metadata.db")
    c = conn.cursor()
    try:
        c.execute("DELETE FROM vinyl WHERE id = :id", {'id': id})
        conn.commit()
        statusMessage = "Vinyl with given ID has been removed."
        return statusMessage
    finally:
        c.close()
        conn.close()


def getAllVinyl():
    conn = sqlite3.connect("./data/metadata.db")
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM vinyl")
        row = c.fetchall()
        result = []
        for x in row:
            vinyl = Vinyl(x[0], x[1], x[2])
            result.append(vinyl)
        return result
    finally:
        c.close()
        conn.close()