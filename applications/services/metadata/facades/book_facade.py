from entities.book import Book


def createBook(book):
    # todo persist to database

    statusMessage = "200 ok"
    return statusMessage


def getBookById(id):
    # todo get from database
    # fixed value for now
    book = Book(id, "title", "author", 10)

    return book


def updateBook(book):
    # todo persist updates to database

    statusMessage = "200 ok"
    return statusMessage


def deleteBookById(id):
    # todo remove persisted data

    statusMessage = "200 ok"
    return statusMessage
