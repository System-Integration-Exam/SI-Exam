import json as JSON
from logic.protogen.warehouse import store_pb2_grpc
from logic.protogen.warehouse import store_pb2
from utils.config import CONFIG
from entities.warehouse.store import Store

import grpc

_CLIENT_CONFIG: str = CONFIG["clients"]["warehouse"]


def _create_stub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return store_pb2_grpc.StoreStub(channel)


def create_store(new_store):
    return _create_stub().CreateStore(
        store_pb2.CreateStoreRequest(
            address=new_store.address,
            phone_number=new_store.phone_number,
            email=new_store.email
        )
    )


def read_store(store_id):
    response =  _create_stub().ReadStore(
        store_pb2.ReadStoreRequest(
            id=store_id
        )
    )
    return JSON.dumps(Store.from_grpc_response(response).__dict__)

def update_store(store_id, store):
    return _create_stub().UpdateStore(
        store_pb2.UpdateStoreRequest(
            id=store_id,
            store=store_pb2.StoreObject(
                address=store.address,
                phone_number=store.phone_number,
                email=store.email
            )
        )
    )

def delete_store(store_id):
    return _create_stub().DeleteStore(
        store_pb2.DeleteStore(
            id=store_id,
        )
    )

def read_store_list():
    response = _create_stub().ReadStoreList(store_pb2.ReadStoreListRequest())
    return JSON.dumps(Store.from_grpc_list_response(response))

def add_book_to_store(store_id, book_id):
    return _create_stub().AddBookToStore(
        store_pb2.AddBookToStoreRequest(
            store_id=store_id,
            book_id=book_id,
        )
    )

def remove_book_from_store(store_id, book_id):
    return _create_stub().RemoveBookFromStore(
        store_pb2.RemoveBookFromStoreRequest(
            store_id=store_id,
            book_id=book_id,
        )
    )

def get_amount_of_specific_book_from_store(store_id, book_id):
    return _create_stub().GetAmountOfSpecificBookFromStore(
        store_pb2.GetAmountOfSpecificBookFromStoreRequest(
            store_id=store_id,
            book_id=book_id,
        )
    )

def add_vinyl_to_store(store_id, vinyl_id):
    return _create_stub().AddVinylToStore(
        store_pb2.AddVinylToStoreRequest(
            store_id=store_id,
            vinyl_id=vinyl_id
        )
    )

def remove_vinyl_from_store(store_id, vinyl_id):
    return _create_stub().RemoveVinylFromStore(
        store_pb2.RemoveVinylFromStoreRequest(
            store_id=store_id,
            vinyl_id=vinyl_id
        )
    )

def get_amount_of_specific_vinyl_from_store(store_id, vinyl_id):
    return _create_stub().GetAmountOfSpecificVinylFromStore(
        store_pb2.GetAmountOfSpecificVinylFromStoreRequest(
            store_id=store_id,
            vinyl_id=vinyl_id
        )
    )



