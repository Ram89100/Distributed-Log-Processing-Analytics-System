from confluent_kafka import Producer as CKProducer
import json


class Producer:
def __init__(self, bootstrap_servers="redpanda:9092"):
self.p = CKProducer({"bootstrap.servers": bootstrap_servers})


def delivery_report(self, err, msg):
if err is not None:
print(f"Delivery failed: {err}")


def produce(self, topic: str, key: str, value: str):
self.p.produce(topic=topic, key=key, value=value, callback=self.delivery_report)
self.p.poll(0)


def flush(self):
self.p.flush()