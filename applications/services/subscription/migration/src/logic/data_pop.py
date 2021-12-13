from entities.customer import Customer
from entities.subscription import Subscription
from faker import Faker
import random


def populate() -> None:
    fake = Faker()
    
    for _ in range(20):
        Customer(fake.first_name(), fake.last_name(), faker.email(), faker.phone_number())
        
    for _ in range(10):
        subscription(random.choice([True, False]), faker.date_time)
        
        

    
    
    
        

