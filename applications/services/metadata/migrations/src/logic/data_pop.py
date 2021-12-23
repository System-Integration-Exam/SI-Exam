from entities.book import Book
from entities.song import Song
from entities.vinyl import Vinyl


def populate() -> None:

    print("populating book data...")

    for book in [
        Book("Dune", "Frank Herbert", 4),
        Book("Harry Potter and the prisoner of Azkaban", "J. K. Rowling", 3),
        Book("The Great Gatsby", "F. Scott Fitzgerald", 5),
    ]:
        book.insert_query()

    print("populating vinyl data...")

    vinylId = "e2983ce3-7b69-47d8-8df1-bf775bfdbe6b"
    for vinyl in [Vinyl(vinylId, "Bon Iver", "Classic Modern")]:
        vinyl.insert_query()

    print("populating song data...")

    for song in [
        Song("Perth", 124, vinylId),
        Song("Minnesota, WI", 352, vinylId),
        Song("Michicant", 458, vinylId)
    ]:
        song.insert_query()
