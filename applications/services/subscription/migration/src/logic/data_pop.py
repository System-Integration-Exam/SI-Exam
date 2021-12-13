from entities.customer import Customer
from entities.subscription import Subscription
from faker import Faker
import random


def populate() -> None:
    faker = Faker()
    
    for _ in range(20):
        Customer(faker.first_name(), faker.last_name(), faker.email(), faker.phone_number())
        
    for _ in range(10):
        Subscription(random.choice([True, False]), faker.date_time)
        
        

    
    
    
        

