import sqlite3
from sqlite3.dbapi2 import Error
from entities.book import Book



def createBook(book):
    conn = sqlite3.connect("./data/metadata.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO book (title, author, rating) VALUES (:title, :author, :rating)", {'title': book.title, 'author': book.author, 'rating': book.rating})
        conn.commit()
        statusMessage = "Book successfully created."
        return statusMessage
    finally:
        c.close()
        conn.close()



def getBookById(id):
    conn = sqlite3.connect("./data/metadata.db")
    c = conn.cursor()
    try:
        c.execute("SELECT * FROM book WHERE id = :id", {'id': id})
        row = c.fetchone()
        book = Book(row[0], row[1], row[2], row[3])
        return book
    finally:
        c.close()
        conn.close()


def updateBook(book):
    conn = sqlite3.connect("./data/metadata.db")
    c = conn.cursor()
    try:
        c.execute("UPDATE book SET title = :title, author = :author, rating = :rating WHERE id = :id", {'id': book.id, 'title': book.title, 'author': book.author, 'rating': book.rating})
        conn.commit()
        statusMessage = "Book successfully updated."
        return statusMessage
    finally:
        c.close()
        conn.close()


def deleteBookById(id):
    conn = sqlite3.connect("./data/metadata.db")
    c = conn.cursor()
    try:
        c.execute("DELETE FROM book WHERE id = :id", {'id': id})
        conn.commit()
        statusMessage = "Book with given ID has been removed."
        return statusMessage
    finally:
        c.close()
        conn.close()
