from confluent_kafka import Producer


# p = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('[Produce] Kafka message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def upload_produce_message(image_name):
    p = Producer({'bootstrap.servers': 'localhost:9092'})
    # p.produce('TutorialTopic', image.encode('utf-8'), callback=delivery_report)
    p.produce('TutorialTopic', image_name.encode('utf-8'), callback=delivery_report)
    
    p.flush()


# some_data_source = ["hell0 1", "hell0 2", "hell0 3"]

# for data in some_data_source:
#     # Trigger any available delivery report callbacks from previous produce() calls
#     p.poll(0)

#     # Asynchronously produce a message, the delivery report callback
#     # will be triggered from poll() above, or flush() below, when the message has
#     # been successfully delivered or failed permanently.
#     p.produce('TutorialTopic', data.encode('utf-8'), callback=delivery_report)

# # Wait for any outstanding messages to be delivered and delivery report
# # callbacks to be triggered.
# p.flush()