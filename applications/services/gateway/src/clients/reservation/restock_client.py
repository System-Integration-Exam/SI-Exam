import json as JSON
from logic.protogen import reservation_pb2_grpc
from logic.protogen import reservation_pb2
from utils.config import CONFIG
from google.protobuf.json_format import MessageToJson


import grpc

_CLIENT_CONFIG: str = CONFIG["clients"]["reservation"]


def _create_stub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return reservation_pb2_grpc.ReservationStub(channel)


def restock(restock_request):
    _create_stub().RequestRestock(
        reservation_pb2.RestockRequest(
            requestText=restock_request["requestText"],
            itemType=restock_request["itemType"],
            existingItemCount=restock_request["existingItemCount"],
            storeId=restock_request["storeId"],
            itemId=restock_request["itemId"],
        )
    )
