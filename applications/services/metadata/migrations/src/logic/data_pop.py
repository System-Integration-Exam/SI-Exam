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
    

    # for store_m2m_book in [
    #     StoreM2MBook(1,2),
    #     StoreM2MBook(1,3),
    #     StoreM2MBook(1,4),
    #     StoreM2MBook(1,5),
    #     StoreM2MBook(1,6),
    #     StoreM2MBook(2,2),
    #     StoreM2MBook(2,2),
    #     StoreM2MBook(2,2),
    #     StoreM2MBook(2,4),
    #     StoreM2MBook(2,7),
    # ]:
    #     store_m2m_book.insert_query()
    
    # for store_m2m_vinyl in [
    #     StoreM2MVinyl(1,3),
    #     StoreM2MVinyl(1,5),
    #     StoreM2MVinyl(1,7),
    #     StoreM2MVinyl(1,4),
    #     StoreM2MVinyl(1,1),
    #     StoreM2MVinyl(2,3),
    #     StoreM2MVinyl(2,5),
    #     StoreM2MVinyl(2,4),
    #     StoreM2MVinyl(2,4),
    #     StoreM2MVinyl(2,1),
    # ]:
    #     store_m2m_vinyl.insert_query()
        
        
    
    
    
        

