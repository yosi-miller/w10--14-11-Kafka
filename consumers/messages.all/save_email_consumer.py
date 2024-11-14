import json

from kafka import KafkaConsumer

from database.mongoDB.repository import insert_email

consumer = KafkaConsumer(
    'save-email-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='email',
    enable_auto_commit=False,
    # value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    # # value_deserializer = lambda x: x.decode('utf-8')
)

print('set up save email consumer')
for email in consumer:
    email = email.value
    print(email)
    print(f"Received email: {email['email']} to save in mongoDB")

    result = insert_email(email)

    if result:
        print(f'Email: {email['email']} save, insert id {result}')
        consumer.commit()