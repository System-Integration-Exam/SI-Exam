from clients.metadata import song_client
from flask import request, current_app
from grpc import RpcError

def create_song():
    try:
        return song_client.create_song(request.json), 201
    except RpcError as e:
        current_app.logger.error("%s", e)
        return e, 502
    except Exception as e:
        current_app.logger.error("%s", e)
        return e, 500


def read_song(id):
    try:
        return song_client.read_song(id)
    except RpcError as e:
        current_app.logger.error("%s", e)
        return e, 502
    except Exception as e:
        current_app.logger.error("%s", e)
        return e, 500


def read_song_list():
    try:
        return song_client.read_song_list()
    except RpcError as e:
        current_app.logger.error("%s", e)
        return e, 502
    except Exception as e:
        current_app.logger.error("%s", e)
        return e, 500


def update_song(id):
    try:
        return song_client.update_song(request.json, id)
    except RpcError as e:
        current_app.logger.error("%s", e)
        return e, 502
    except Exception as e:
        current_app.logger.error("%s", e)
        return e, 500


def delete_song(id):
    try:
        return song_client.delete_song(id)
    except RpcError as e:
        current_app.logger.error("%s", e)
        return e, 502
    except Exception as e:
        current_app.logger.error("%s", e)
        return e, 500


def collect_routes(app):
    app.add_url_rule("/song", view_func=create_song, methods=["POST"])
    app.add_url_rule("/song/<string:id>", view_func=read_song, methods=["GET"])
    app.add_url_rule("/song", view_func=read_song_list, methods=["GET"])
    app.add_url_rule("/song/<string:id>", view_func=update_song, methods=["PUT"])
    app.add_url_rule("/song/<string:id>", view_func=delete_song, methods=["DELETE"])
