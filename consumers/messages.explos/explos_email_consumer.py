import json
from kafka import KafkaConsumer
from database.PostgreSQL.postgresql_repository import insert_explos_email_reference


consumer = KafkaConsumer(
    'explos-email-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='email',
    enable_auto_commit=False,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

print('set up save email id in explos table')

for email_id in consumer:
    email_id = email_id.value
    print(f"Received email ID: {email_id} to save in explos table")

    result = insert_explos_email_reference(email_id)

    if result:
        print(f'Email ID: {email_id} save, insert id {result}')
        consumer.commit()