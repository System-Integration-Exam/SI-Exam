import json as JSON
from logic.protogen import vinyl_pb2_grpc
from logic.protogen import vinyl_pb2
from utils.config import CONFIG
from google.protobuf.json_format import MessageToJson
from entities.link import Link


import grpc

_CLIENT_CONFIG: str = CONFIG["clients"]["metadata"]


def _create_stub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return vinyl_pb2_grpc.VinylStub(channel)


def create_vinyl(new_vinyl_json):

    vinyl = (
        _create_stub()
        .createVinyl(
            vinyl_pb2.CreateVinylRequest(
                artist=new_vinyl_json["artist"],
                genre=new_vinyl_json["genre"],
            )
        )
        .vinyl
    )
    return JSON.dumps(
        {
            "id": vinyl.id,
            "artist": vinyl.artist,
            "genre": vinyl.genre,
        }
    )


def read_vinyl(vinyl_id):
    response = _create_stub().readVinyl(vinyl_pb2.ReadVinylRequest(id=vinyl_id))
    return {
        "payload": {"artist": response.artis, "genre": response.genre},
        "links":[
            Link("this vinyl", f"/vinyl/{response.id}").__dict__, 
            Link("all vinyls", "/vinyl").__dict__
        ],
    }


def read_vinyl_list():
    response = _create_stub().readVinylList(vinyl_pb2.ReadVinylListRequest())
    vinyls = [
        {   
            "payload":{
                "id": vinyl.id,
                "artist": vinyl.artist,
                "genre": vinyl.genre
            },
            "links":[
                Link("this vinyl", f"/vinyl/{vinyl.id}").__dict__, 
                Link("all vinyls", "/vinyl").__dict__
            ]
        }
        for vinyl in response.vinyl_list
    ]
    return JSON.dumps(vinyls)


def update_vinyl(update_vinyl_json, id):
    return (
        _create_stub()
        .updateVinyl(
            vinyl_pb2.UpdateVinylRequest(
                id=id,
                artist=new_vinyl_json["artist"],
                genre=new_vinyl_json["genre"],
            )
        )
        .msg
    )


def delete_vinyl(vinyl_id):
    response = _create_stub().DeleteVinyl(vinyl_pb2.DeleteVinylRequest(id=vinyl_id))
    return MessageToJson(response)
