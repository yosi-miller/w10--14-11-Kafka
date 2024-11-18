from database.PostgreSQL.models import EmailsModel, HostageModel, ExplosModel
from database.PostgreSQL.postgre_sql_connection import db_session

def my_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error occurred while processing email: {kwargs.get('email')}")
            print(e)
            return e
        finally:
            db_session.close()
    return wrapper

@my_decorator
def insert_danger_email(e):
    new_email = EmailsModel(
        email=e["email"],
        username=e["username"],
        ip_address=e["ip_address"],
        created_at=e["created_at"],
        location=e["location"],
        device_info=e["device_info"],
        sentences=e["sentences"]
    )

    db_session.add(new_email)
    db_session.commit()

    return new_email.id

@my_decorator
def insert_hostage_email_reference(email_id):
    new_hostage_reference = HostageModel(
        email_id=email_id
    )

    db_session.add(new_hostage_reference)
    db_session.commit()

    return new_hostage_reference.id

@my_decorator
def insert_explos_email_reference(email_id):
    new_explos_reference = ExplosModel(
        email_id=email_id
    )

    db_session.add(new_explos_reference)
    db_session.commit()

    return new_explos_reference.id

@my_decorator
def get_sentences_by_email(email):
    return db_session.query(EmailsModel).filter_by(email=email).all()

@my_decorator
def get_all_sentences():
    return db_session.query(EmailsModel).all()


if __name__ == '__main__':
    print(get_all_sentences())