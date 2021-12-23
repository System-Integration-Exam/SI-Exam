from kafka import KafkaConsumer
from json import loads
from logic.handlers.customer_handler import camel_populate_customer
from utils.config import CONFIG

def kafka_consumer() -> None:
    consumer = KafkaConsumer(
        "subscriptionserviceuserlistupdate-topic",
        bootstrap_servers=[CONFIG["kafka"]["broker"]],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="subscriptionservice",
        value_deserializer=lambda x: loads(x.decode("utf-8")),
    )
    for message in consumer:
        for data in message.value[1:]:
            camel_populate_customer(data)
