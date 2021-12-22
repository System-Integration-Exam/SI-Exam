import json as JSON
from logic.protogen import store_pb2_grpc
from logic.protogen import store_pb2
from utils.config import CONFIG
from entities.warehouse.store import Store
from google.protobuf.json_format import MessageToJson
from entities.link import Link

import grpc

_CLIENT_CONFIG: str = CONFIG["clients"]["warehouse"]


def _create_stub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return store_pb2_grpc.StoreStub(channel)


def create_store(new_store_json):
    return (
        _create_stub()
        .CreateStore(
            store_pb2.CreateStoreRequest(
                address=new_store_json["address"],
                phone_number=new_store_json["phone_number"],
                email=new_store_json["email"],
            )
        )
        .msg
    )


def read_store(store_id):
    response = _create_stub().ReadStore(store_pb2.ReadStoreRequest(id=store_id)).store
    return {
        "payload":{
            "address": response.address,
            "phone_number": response.phone_number,
            "email": response.email,
            "created_at": response.created_at,
            "updated_at": response.updated_at,
        },
        "links":[
            Link("this store", f"/store/{store_id}"),
            Link("all stores", "/store")
        ]
    }


def update_store(store_id, store_json):
    return (
        _create_stub()
        .UpdateStore(
            store_pb2.UpdateStoreRequest(
                id=store_id,
                address=store_json["address"],
                phone_number=store_json["phone_number"],
                email=store_json["email"],
            )
        )
        .msg
    )


def update_store_by_address(address_match, store):
    return (
        _create_stub()
        .UpdateStore(
            store_pb2.UpdateStoreRequest(
                address_match=address_match,
                address_update=store["address"],
                phone_number=store["phone_number"],
                email=store["email"],
            )
        )
        .msg
    )


def delete_store(store_id):
    return (
        _create_stub()
        .DeleteStore(
            store_pb2.DeleteStoreRequest(
                id=store_id,
            )
        )
        .msg
    )


def delete_store_by_address(address):
    return (
        _create_stub()
        .DeleteStoreByAddress(store_pb2.DeleteStoreByAddressRequest(address=address))
        .msg
    )


def read_store_list():
    response = _create_stub().ReadStoreList(store_pb2.ReadStoreListRequest())
    stores = [
        {
            "payload": Store.from_grpc_response(store).__dict__,
            "links": [
                Link("all books", f"/book").__dict__,
                Link("all vinyls", f"/vinyl").__dict__,
                Link("all songs", f"/song").__dict__,
                Link("all stores", f"/store").__dict__,
                
            ],
        }
        for store in response.store_list
    ]
    return JSON.dumps(stores)


################


def add_book_to_store(store_id, book_id):
    return (
        _create_stub()
        .AddBookToStore(
            store_pb2.AddBookToStoreRequest(
                store_id=store_id,
                book_id=book_id,
            )
        )
        .msg
    )


def remove_book_from_store(store_id, book_id):
    return (
        _create_stub()
        .RemoveBookFromStore(
            store_pb2.RemoveBookFromStoreRequest(
                store_id=store_id,
                book_id=book_id,
            )
        )
        .msg
    )


def get_amount_of_specific_book_from_store(store_id, book_id):
    return (
        _create_stub()
        .GetAmountOfSpecificBookFromStore(
            store_pb2.GetAmountOfSpecificBookFromStoreRequest(
                store_id=store_id,
                book_id=book_id,
            )
        )
        .amount
    )


##########


def add_vinyl_to_store(store_id, vinyl_id):
    return (
        _create_stub()
        .AddVinylToStore(
            store_pb2.AddVinylToStoreRequest(store_id=store_id, vinyl_id=vinyl_id)
        )
        .msg
    )


def remove_vinyl_from_store(store_id, vinyl_id):
    return (
        _create_stub()
        .RemoveVinylFromStore(
            store_pb2.RemoveVinylFromStoreRequest(store_id=store_id, vinyl_id=vinyl_id)
        )
        .msg
    )


def get_amount_of_specific_vinyl_from_store(store_id, vinyl_id):
    return (
        _create_stub()
        .GetAmountOfSpecificVinylFromStore(
            store_pb2.GetAmountOfSpecificVinylFromStoreRequest(
                store_id=store_id, vinyl_id=vinyl_id
            )
        )
        .amount
    )


########


def return_item_stock_info(uuid: str, store_id: int):
    return (
        _create_stub()
        .ReturnItemStockInfo(
            store_pb2.ReturnItemStockInfoRequest(
                uuid=uuid,
                store_id=store_id,
            )
        )
        .msg
    )
