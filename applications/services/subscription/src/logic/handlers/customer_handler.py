from connection.sqlite_connection import execute_query, fetch_one
from logic.protogen import customer_pb2


def create_customer(
    request: customer_pb2.CreateCustomerRequest,
) -> customer_pb2.CreateCustomerResponse:
    try:
        execute_query(
            f"""
                      INSERT INTO customer(first_name, last_name, email, phone_number)
                      VALUES ('{request.first_name}','{request.last_name}', '{request.email}', '{request.phone_number}')
                      """
        )
        return customer_pb2.CreateCustomerResponse(msg="Ok")
    except Exception as e:
        print(e)
        return customer_pb2.CreateCustomerResponse(msg="Err: Could not execute query")


def read_customer(
    request: customer_pb2.ReadCustomerRequest,
) -> customer_pb2.ReadCustomerResponse:
    try:
        res = fetch_one(
            f"""
                      SELECT * FROM customer
                      WHERE id = {int(request.id)}
                      """
        )
        return customer_pb2.ReadCustomerResponse(
            id=res[0],
            first_name=res[1],
            last_name=res[2],
            email=res[3],
            phone_number=res[4],
        )
    except Exception as e:
        print(e)
        return customer_pb2.ReadCustomerResponse(
            customer_pb2.ReadCustomerResponse(
                id=-1,
                first_name="",
                last_name="",
                email="",
                phone_number="",
            )
        )


def update_customer(
    request: customer_pb2.UpdateCustomerRequest,
) -> customer_pb2.UpdateCustomerResponse:
    try:
        execute_query(
            f"""
                      UPDATE customer
                      SET (first_name, last_name, email, phone_number) = ('{request.first_name}','{request.last_name}', '{request.email}', '{request.phone_number}')
                      WHERE id = {int(request.id)}
                      """
        )
        return customer_pb2.UpdateCustomerResponse(msg="Ok")
    except Exception as e:
        print(e)
        return customer_pb2.UpdateCustomerResponse(msg="Err: Could not execute query")
