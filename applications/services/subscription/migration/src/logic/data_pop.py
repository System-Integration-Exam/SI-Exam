from entities.customer import Customer
from entities.subscription import Subscription
from faker import Faker
import random


def populate() -> None:
    # faker = Faker()

    # for _ in range(10):
    #     Subscription(random.choice([True, False]), faker.date_time()).insert_query()

    # for customer in range(20):
    #     Customer(
    #         random.randrange(1, 10),
    #         faker.first_name(),
    #         faker.last_name(),
    #         faker.email(),
    #         faker.phone_number(),
    #     ).insert_query()
    print("populating")
