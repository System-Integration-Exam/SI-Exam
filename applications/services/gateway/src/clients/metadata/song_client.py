import json as JSON
from logic.protogen import song_pb2_grpc
from logic.protogen import song_pb2
from utils.config import CONFIG
from google.protobuf.json_format import MessageToJson
from entities.link import Link


import grpc

_CLIENT_CONFIG: str = CONFIG["clients"]["metadata"]


def _create_stub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return song_pb2_grpc.SongStub(channel)


def create_song(new_song_json):

    song = (
        _create_stub()
        .createSong(
            song_pb2.CreateSongRequest(
                title=new_song_json["title"],
                duration_sec=new_song_json["duration_sec"],
                vinyl_id=new_song_json["vinyl_id"],
            )
        )
        .song
    )

    return JSON.dumps(
        {
            "id": song.id,
            "title": song.title,
            "duration_sec": song.duration_sec,
            "vinyl_id": song.vinyl_id,
        }
    )


def read_song(song_id):
    response = _create_stub().readSong(song_pb2.ReadSongRequest(id=song_id))
    return {
        "payload": {
            "title": response.title,
            "duration_sec": response.duration_sec,
            "vinyl_id": response.vinyl_id,
        },
        "links": [
            Link("this song", f"/song/{response.id}").__dict__, 
            Link("all songs", f"/song").__dict__
        ],
    }


def read_song_list():
    response = _create_stub().readSongList(song_pb2.ReadSongListRequest())
    songs = [
        {
            "payload": {
                "id": song.id,
                "title": song.title,
                "duration_sec": song.duration_sec,
                "vinyl_id": song.vinyl_id,
            },
            "links": [
                Link("this song", f"/song/{song.id}").__dict__, 
                Link("all songs", "/song").__dict__
            ],
        }
        for song in response.song_list
    ]
    return JSON.dumps(songs)


def update_song(update_song_json, id):
    return (
        _create_stub()
        .updateSong(
            song_pb2.UpdateSongRequest(
                id=id,
                title=new_song_json["title"],
                duration_sec=new_song_json["duration_sec"],
                vinyl_id=new_song_json["vinyl_id"],
            )
        )
        .msg
    )


def delete_song(song_id):
    response = _create_stub().deleteSong(song_pb2.DeleteSongRequest(id=song_id))
    return MessageToJson(response)
