from confluent_kafka import Consumer, KafkaError
from confluent_kafka import Producer
import json
import numpy as np

# def produce_message2(data):
#   p = Producer({'bootstrap.servers': 'localhost:9092'})
#   p.poll(0)
#   p.produce("TutorialTopic2", data.encode('utf-8'))
#   p.flush()

class ConsumerClient:
    
    def __init__(self):

        self.c = Consumer({
            'bootstrap.servers': 'localhost:9092',
            'group.id': 'mygroup',
            'auto.offset.reset': 'earliest'
        })
        self.c.subscribe(['TutorialTopic'])

    def consume_message(self):
        # Kafka consumer
        while True:
            msg = self.c.poll(timeout=1.0)

            if msg is None:
                continue
            if msg.error():
                print("Consumer error: {}".format(msg.error()))
                continue
            
            else:
                print('[Consume] Kafka message: {}'.format(msg.value()))
                return msg.value()
            

    def __del__(self):
        self.c.close()
    