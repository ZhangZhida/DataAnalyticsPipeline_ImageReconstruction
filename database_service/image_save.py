from confluent_kafka import Consumer, KafkaError
from confluent_kafka import Producer
import json
import numpy as np

# def produce_message2(data):
#   p = Producer({'bootstrap.servers': 'localhost:9092'})
#   p.poll(0)
#   p.produce("TutorialTopic2", data.encode('utf-8'))
#   p.flush()


c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})


c.subscribe(['TutorialTopic'])

while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue
    
    print('Received message: {}'.format(msg.value()))
    # produce_message2(json.dumps(data))


c.close()