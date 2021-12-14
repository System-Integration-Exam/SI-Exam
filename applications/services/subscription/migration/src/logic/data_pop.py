from entities.customer import Customer
from entities.subscription import Subscription
from faker import Faker
import random


def populate() -> None:
    faker = Faker()
    
    for customer in range(20):
        Customer(faker.first_name(), faker.last_name(), faker.email(), faker.phone_number()).insert_query()

        
    for _ in range(10):
        Subscription(random.choice([True, False]), faker.date_time).insert_query()
        
        

    
    
    
        

