from database.mongoDB.mongo_connection import get_database

db = get_database()
email_list_collection = db['all_email']

def insert_email(email):
    try:
        result = email_list_collection.insert_one(email)
    except Exception as e:
        print(f"Error inserting email {email} to the black list")
        return False
    return result.inserted_id

def get_all_emails():
    return list(email_list_collection.find({}, {'_id': 0}).limit(25))