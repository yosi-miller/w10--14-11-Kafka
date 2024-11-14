import json
from kafka import KafkaProducer
from database.PostgreSQL.postgresql_repository import insert_danger_email
from producer.producer_repository import dangerous_sentences_checker

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8')  # המרה ל-JSON ואז ל-bytes
                         )


def processor_management(email):
    producer.send('save-email-topic', email)
    print(f'Email {email["email"]} sent to save in database')

    # Check if the email contains any dangerous sentences
    print(f'Start check if have any word dangerous in the {email["email"]} sentences')
    email, hostage_status, explos_status = dangerous_sentences_checker(email)

    if hostage_status or explos_status:
        save_danger_email = insert_danger_email(email)
        if hostage_status:
            producer.send('hostage-email-topic', save_danger_email)
        if explos_status:
            producer.send('explos-email-topic', save_danger_email)

    producer.flush() # producer.flush is used to make sure that all messages are sent before closing the producer
