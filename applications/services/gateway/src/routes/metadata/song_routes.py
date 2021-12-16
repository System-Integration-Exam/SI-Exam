from clients.metadata import song_client
from flask import request


def create_song():
    try:
        return song_client.create_song(request.json)
    except Exception as e:
        print(e)
        return "500"


def read_song(id):
    try:
        return song_client.read_song(id)
    except Exception as e:
        print(f"Error: {e}")
        return "500"


def read_song_list():
    try:
        return song_client.read_song_list()
    except Exception as e:
        print(f"Error: {e}")
        return "500"


def update_song(id):
    try:
        return song_client.update_song(request.json, id)
    except Exception as e:
        print(e)
        return "500"


def delete_song(id):
    try:
        return song_client.delete_song(id)
    except Exception as e:
        print(f"Error: {e}")
        return "500"


def collect_routes(app):
    app.add_url_rule("/song", view_func=create_song, methods=["POST"])
    app.add_url_rule("/song/<int:id>", view_func=read_song, methods=["GET"])
    app.add_url_rule("/song", view_func=read_song_list, methods=["GET"])
    app.add_url_rule("/song/<int:id>", view_func=update_song, methods=["PUT"])
    app.add_url_rule(
        "/song/<int:id>", view_func=delete_song, methods=["DELETE"]
    )
