from confluent_kafka import Consumer, KafkaError
from confluent_kafka import Producer
import json
import numpy as np

class ConsumerClient:
    
    def __init__(self):

        localhost = 'localhost'
        gcp_host = '35.230.175.86'
        self.c = Consumer({
            'bootstrap.servers': localhost +':9092', # GCP instance running Kafka server
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
    