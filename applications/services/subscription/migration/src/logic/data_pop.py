from entities.customer import Customer
from entities.subscription import Subscription
from faker import Faker
import random


def populate() -> None:
    faker = Faker()

    print("populating subscription data...")

    for _ in range(5):
        Subscription(random.choice([True, False]), faker.date_time()).insert_query()

    print("populating customer data...")

    for sub_id in range(5):
        Customer(
            sub_id,
            faker.first_name(),
            faker.last_name(),
            faker.email(),
            faker.phone_number(),
        ).insert_query()
    
