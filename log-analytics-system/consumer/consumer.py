import json
from confluent_kafka import Consumer, KafkaException
from processor import process_log
import os


KAFKA_BOOTSTRAP = os.getenv("KAFKA_BOOTSTRAP", "redpanda:9092")


conf = {
'bootstrap.servers': KAFKA_BOOTSTRAP,
'group.id': 'log-consumers',
'auto.offset.reset': 'earliest'
}


c = Consumer(conf)


def main():
c.subscribe(['logs_raw'])
try:
while True:
msg = c.poll(1.0)
if msg is None:
continue
if msg.error():
raise KafkaException(msg.error())
process_log(msg.value().decode('utf-8'))
except KeyboardInterrupt:
pass
finally:
c.close()


if __name__ == '__main__':
main()