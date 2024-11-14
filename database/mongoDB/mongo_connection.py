from pymongo import MongoClient


def get_database():
    mongo_uri = "mongodb://localhost:27017"

    client = MongoClient(mongo_uri)

    return client['email_db']


