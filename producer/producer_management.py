import json

from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8')  # המרה ל-JSON ואז ל-bytes
                         )


def processor_management(email):
    print(type(email))
    producer.send('save-email-topic', email)
    print(f'Email {email["email"]} sent to save in database')

    producer.flush() # producer.flush is used to make sure that all messages are sent before closing the producer
