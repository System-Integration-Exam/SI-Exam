
from entities.book import Book

def getBookInfo(x):
    #todo get from database
    #fixed value for now
    book = Book(10, "title", "author", 10) 

    return book


def create():
    return 0

def read():
    return 0

def update():
    return 0
    
def delete():
    return 0


print(getBookInfo(10))