
from logic.protogen import user_pb2_grpc
from logic.protogen import user_pb2
from utils.config import CONFIG
from models.user import User

import grpc

_CLIENT_CONFIG: str = CONFIG["grpc"]


def _create_stub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return user_pb2_grpc.UserStub(channel)
