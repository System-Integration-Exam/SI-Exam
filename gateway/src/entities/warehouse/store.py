from dataclasses import dataclass
from entities.link import Link

@dataclass
class NewStore():
    address: str
    phone_number: str
    email: str
        
    @staticmethod
    def from_json(data):
        return NewStore(
            address = data.get('address'),
            phone_number= data.get('phone_number'),
            email = data.get('email'),
        )
    
@dataclass    
class Store():
    address: str
    phone_number: str
    email: str
    created_at:str
    updated_at: str
    
        
    @staticmethod
    def from_grpc_response(response):
        return Store(
            address = response.address,
            phone_number = response.phone_number,
            email = response.email,
            updated_at = response.updated_at,
            created_at = response.created_at
        )
        
    @staticmethod
    def from_grpc_response_list(response):
        store_list = []
        for store in response.store_list:
            store_list.append(Store.from_grpc_response(store).__dict__)
        return store_list
        

    
@dataclass
class StoreLinked():
    store: Store
    link: Link