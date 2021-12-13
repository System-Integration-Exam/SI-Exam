from sqlite_connection import execute_query, fetch_one
from logic.protogen import customer_pb2


def create_customer(request: customer_pb2.CreateCustomerRequest) -> customer_pb2.CreateCustomerResponse:
    try:
        execute_query(f"""
                      INSERT INTO customer(first_name, last_name, email, phone_number)
                      VALUES ('{request.first_name}','{request.last_name}', '{request.email}', '{request.phone_number}')
                      """)
        return customer_pb2.CreateCustomerResponse(msg="Ok")
    except Exception as e:
        print(e)
        return customer_pb2.CreateCustomerResponse(msg="Err: Could not execute query")


def read_customer(request: customer_pb2.ReadCustomerRequest) -> customer_pb2.ReadCustomerResponse:
    try:
        res = fetch_one(f"""
                      INSERT INTO customer(first_name, last_name, email, phone_number)
                      VALUES ('{request.first_name}','{request.last_name}', '{request.email}', '{request.phone_number}')
                      """)
        return customer_pb2.ReadCustomerResponse(customer_pb2.ReadCustomerResponse(
            id=res["id"],
            first_name=res["first_name"],
            last_name=res["last_name"],
            email=res["email"],
            phone_number=res["phone_number"]
        ))
    except Exception as e:
        print(e)
        return customer_pb2.ReadCustomerResponse(customer_pb2.ReadCustomerResponse(
            id=-1,
            first_name="",
            last_name="",
            email="",
            phone_number="",
        ))
        
        

