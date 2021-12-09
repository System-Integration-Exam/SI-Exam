
from entities.Book import Book

def getBookInfo(x):
    #todo get from database
    #fixed value for now
    book = Book(10, "title", "author", 10) 

    return book


print(getBookInfo(10))