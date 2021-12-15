from entities.book import Book
from entities.song import Song
from entities.vinyl import Vinyl



def populate() -> None:
    for book in [
        Book("Dune", "Frank Herbert", 4),
        Book("Harry Potter and the prisoner of Azkaban", "J. K. Rowling", 3),
        Book("The Great Gatsby", "F. Scott Fitzgerald", 5),
    ]:
        book.insert_query()
    
    for vinyl in [
        Vinyl("Bon Iver", "Classic Modern")
    ]:
        vinyl.insert_query()

    #todo, get bon iver vinyl_id

    # for song in [
    #     Song("Perth", 124),
    #     Song("Minnesota, WI", 352),
    #     Song("Michicant", 458,)
    # ]:
    #     song.insert_query()
        
        
        
    
    
    
        

