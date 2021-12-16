import grpc
from concurrent import futures
import time


# import the generated classes
import protogen.book_pb2 as book_pb2
import protogen.book_pb2_grpc as book_pb2_grpc
import protogen.song_pb2 as song_pb2
import protogen.song_pb2_grpc as song_pb2_grpc
import protogen.vinyl_pb2 as vinyl_pb2
import protogen.vinyl_pb2_grpc as vinyl_pb2_grpc


# import the facades
import logic.facades.book_facade as BF
import logic.facades.song_facade as SF
import logic.facades.vinyl_facade as VF


# Book Servicer
class BookServicer(book_pb2_grpc.BookServicer):
    # takes in a book object and returns a status message (success/error)
    def createBook(self, request, context):
        response = None
        try:
            book = BF.createBook(request)
            response = book_pb2.CreateBookResponse(
                book=book_pb2.BookMessage(
                    id=book[0],
                    title=book[1],
                    author=book[2],
                    rating=book[3],
                )
            )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Something went wrong with creating the book")
        return response

    # takes in an ID value and returns a book object
    def getBookById(self, request, context):
        response = book_pb2.GetBookByIdResponse()
        try:
            book = BF.getBookById(request.id)
            response.id = book.id
            response.title = book.title
            response.author = book.author
            response.rating = book.rating
        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Something went wrong with getting the book")
        return response

    # takes in a book object and returns status message
    def updateBook(self, request, context):
        response = book_pb2.UpdateBookResponse()
        try:
            response.statusMessage = BF.updateBook(request)
        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Something went wrong with updating the book")
        return response

    # takes in an ID value and returns status message
    def deleteBookById(self, request, context):
        response = book_pb2.DeleteBookByIdResponse()
        try:
            response.statusMessage = BF.deleteBookById(request.id)
            return response
        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Something went wrong with updating the book")
        return response

    # takes no parameter and returns list of book objects
    def getAllBooks(self, request, context):
        response = book_pb2.GetAllBooksResponse()
        try:
            allBooks = BF.getAllBooks()
            for x in allBooks:
                bookmsg = book_pb2.BookMessage(
                    id=x.id, title=x.title, author=x.author, rating=x.rating
                )
                response.books.append(bookmsg)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Something went wrong with retrieving the data")
        return response


# Song Servicer
class SongServicer(song_pb2_grpc.SongServicer):
    # takes in a song object and returns a status message (success/error)
    def createSong(self, request, context):
        # response = song_pb2.CreateSongResponse()
        response = None
        try:
            song = SF.createSong(request)
            response = song_pb2.CreateSongResponse(
                song=song_pb2.SongMessage(
                    id=song[0],
                    title=song[1],
                    duration_sec=song[2],
                    vinyl_id=song[3],
                )
            )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Something went wrong with creating the song")
        return response

    # takes in an ID value and returns a song object
    def getSongById(self, request, context):
        response = song_pb2.GetSongByIdResponse()
        try:
            song = SF.getSongById(request.id)
            response.id = song.id
            response.title = song.title
            response.duration_sec = song.duration_sec
            response.vinyl_id = song.vinyl_id
        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Something went wrong with getting the book")
        return response

    # takes in a song object and returns status message
    def updateSong(self, request, context):
        response = song_pb2.UpdateSongResponse()
        try:
            response.statusMessage = SF.updateSong(request)
        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Something went wrong with updating the book")
        return response

    # takes in an ID value and returns status message
    def deleteSongById(self, request, context):
        response = song_pb2.DeleteSongByIdResponse()
        try:
            response.statusMessage = SF.deleteSongById(request.id)
        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Something went wrong with updating the book")
        return response

    # takes no parameter and returns list of song objects
    def getAllSongs(self, request, context):
        response = song_pb2.GetAllSongsResponse()
        try:
            allSongs = SF.getAllSongs()
            for x in allSongs:
                songmsg = song_pb2.SongMessage(
                    id=x.id,
                    title=x.title,
                    duration_sec=x.duration_sec,
                    vinyl_id=x.vinyl_id,
                )
                response.songs.append(songmsg)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Something went wrong with retrieving the data")
        return response


# Vinyl Servicer
class VinylServicer(vinyl_pb2_grpc.VinylServicer):
    # takes in a vinyl object and returns a status message (success/error)
    def createVinyl(self, request, context):
        response = None
        try:
            #response = vinyl_pb2.CreateVinylResponse()
            #response.statusMessage = VF.createVinyl(request)
            vinyl = VF.createVinyl(request)
            response = vinyl_pb2.CreateVinylResponse(
                vinyl=vinyl_pb2.VinylMessage(
                    id=vinyl[0],
                    artist=vinyl[1],
                    genre=vinyl[2],
                )
            )
        except Exception as e:
            print(e)
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Something went wrong with creating the vinyl")
        return response

    # takes in an ID value and returns a vinyl object
    def getVinylById(self, request, context):
        response = vinyl_pb2.GetVinylByIdResponse()
        try:
            vinyl = VF.getVinylById(request.id)
            response.id = vinyl.id
            response.artist = vinyl.artist
            response.genre = vinyl.genre
        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Something went wrong with getting the vinyl")
        return response

    # takes in a vinyl object and returns status message
    def updateVinyl(self, request, context):
        response = vinyl_pb2.UpdateVinylResponse()
        try:
            response.statusMessage = VF.updateVinyl(request)
        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Something went wrong with updating the vinyl")
        return response

    # takes in an ID value and returns status message
    def deleteVinylById(self, request, context):
        response = vinyl_pb2.DeleteVinylByIdResponse()
        try:
            response.statusMessage = VF.deleteVinylById(request.id)
        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Something went wrong with updating the vinyl")
        return response

        # takes no parameter and returns list of song objects

    # takes no parameter and returns list of vinyl objects
    def getAllVinyl(self, request, context):
        response = vinyl_pb2.GetAllVinylResponse()
        try:
            allVinyls = VF.getAllVinyl()
            for x in allVinyls:
                vinylmsg = vinyl_pb2.VinylMessage(
                    id=x.id, artist=x.artist, genre=x.genre
                )
                response.vinyls.append(vinylmsg)
        except Exception:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details("Something went wrong with retrieving the data")
        return response


# create gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))


# use the generated function `add_BookServicer_to_server`
# to add the defined class to the server
book_pb2_grpc.add_BookServicer_to_server(BookServicer(), server)
song_pb2_grpc.add_SongServicer_to_server(SongServicer(), server)
vinyl_pb2_grpc.add_VinylServicer_to_server(VinylServicer(), server)

# listen on port 20070
print("Starting server. Listening on port 20070.")
server.add_insecure_port("0.0.0.0:20070")
server.start()


# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
