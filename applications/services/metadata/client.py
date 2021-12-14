import grpc

# import the generated classes
import protogen.book_pb2 as book_pb2
import protogen.book_pb2_grpc as book_pb2_grpc
import protogen.song_pb2 as song_pb2
import protogen.song_pb2_grpc as song_pb2_grpc
import protogen.vinyl_pb2 as vinyl_pb2
import protogen.vinyl_pb2_grpc as vinyl_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel("localhost:50051")

# create a stub (client)
bookStub = book_pb2_grpc.BookStub(channel)
songStub = song_pb2_grpc.SongStub(channel)
vinylStub = vinyl_pb2_grpc.VinylStub(channel)

# create a valid request message
bookId = book_pb2.GetBookByIdRequest(id="asbsabbdabs-asdoaoisdoi-asidoajsodi-asjdaosd")
songId = song_pb2.GetSongByIdRequest(id="asbsabbdabs-asdoaoisdoi-asidoajsodi-asjdaosd")
vinylId = vinyl_pb2.GetVinylByIdRequest(
    id="asbsabbdabs-asdoaoisdoi-asidoajsodi-asjdaosd"
)

# make the call
bookResponse = bookStub.getBookById(bookId)
songResponse = songStub.getSongById(songId)
vinylResponse = vinylStub.getVinylById(vinylId)

# et voilà
print("")
print("")
print("Book :")
print(bookResponse)
print("Song :")
print(songResponse)
print("Vinyl :")
print(vinylResponse)
print("")
print("")
