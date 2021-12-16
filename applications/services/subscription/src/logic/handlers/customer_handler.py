import random
from connection.sqlite_connection import execute_query, fetch_all, fetch_one
from logic.protogen import customer_pb2


def camel_populate_customer(data):
    try:
        execute_query(
            f"""
                    INSERT INTO customer(subscription_id, first_name, last_name, email, phone_number)
                    VALUES ({random.randrange(1, 10)},'{data[1]}','{data[2]}','{data[3]}', '{data[4]}')
            """
        )
        return customer_pb2.CreateCustomerResponse(msg="Ok")
    except Exception as e:
        print(e)
        return customer_pb2.CreateCustomerResponse(msg="Err: Could not execute query")



def create_customer(
    request: customer_pb2.CreateCustomerRequest,
) -> customer_pb2.CreateCustomerResponse:
    try:
        execute_query(
            f"""
                INSERT INTO customer(subscription_id, first_name, last_name, email, phone_number)
                VALUES ('{request.subscription_id}','{request.first_name}','{request.last_name}', '{request.email}', '{request.phone_number}')
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
            subscription_id=res[1],
            first_name=res[2],
            last_name=res[3],
            email=res[4],
            phone_number=res[5],
            created_at=res[6],
            updated_at=res[7],
        )
    except Exception as e:
        print(e)
        return customer_pb2.ReadCustomerResponse(
            id=-1,
            subscription_id=-1,
            first_name="",
            last_name="",
            email="",
            phone_number="",
            created_at="",
            updated_at="",
            
        )


def read_customer_list(
    request: customer_pb2.ReadCustomerListRequest,
) -> customer_pb2.ReadCustomerListResponse:
    try:
        res = fetch_all("SELECT * FROM customer")
        customer_objects = []
        for customer in res:
            cust = customer_pb2.ReadCustomerListResponse.CustomerObject(
                id=customer[0],
                subscription_id=customer[1],
                first_name=customer[2],
                last_name=customer[3],
                email=customer[4],
                phone_number=customer[5],
                created_at=customer[6],
                updated_at=customer[7],
                
            )
            customer_objects.append(cust)

        return customer_pb2.ReadCustomerListResponse(customer_list=customer_objects)
    except Exception as e:
        print(e)
        return customer_pb2.ReadCustomerListResponse(customer_list=[])


def update_customer(
    request: customer_pb2.UpdateCustomerRequest,
) -> customer_pb2.UpdateCustomerResponse:
    try:
        execute_query(
            f"""
                      UPDATE customer
                      SET (subscription_id,first_name, last_name, email, phone_number) = ('{request.subscription_id}','{request.first_name}','{request.last_name}', '{request.email}', '{request.phone_number}')
                      WHERE id = {int(request.id)}
                      """
        )
        return customer_pb2.UpdateCustomerResponse(msg="Ok")
    except Exception as e:
        print(e)
        return customer_pb2.UpdateCustomerResponse(msg="Err: Could not execute query")


def delete_customer(
    request: customer_pb2.DeleteCustomerRequest,
) -> customer_pb2.DeleteCustomerResponse:
    try:
        execute_query(
            f"""
                      DELETE FROM customer
                      WHERE id = {int(request.id)}
                      """
        )
        return customer_pb2.DeleteCustomerResponse(msg="customer deleted")
    except Exception as e:
        print(e)
        return customer_pb2.DeleteCustomerResponse(
            msg="Err: an error occurred. please try again"
        )
