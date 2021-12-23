from logic.protogen.restock_pb2_grpc import RestockGrpcStub
from logic.protogen import restock_pb2
from utils.config import CONFIG

import grpc

_CLIENT_CONFIG: str = CONFIG["clients"]["restock"]


def _create_stub() -> RestockGrpcStub:
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return RestockGrpcStub(channel)


def make_restock_request(restock_request):
    _create_stub().RequestRestock(
        restock_pb2.RestockRequest(
            requestText=restock_request["requestText"],
            itemType=restock_request["itemType"],
            existingItemCount=restock_request["existingItemCount"],
            storeId=restock_request["storeId"],
            itemId=restock_request["itemId"],
        )
    )
