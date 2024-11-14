from database.PostgreSQL.models import EmailsModel, HostageModel, ExplosModel
from database.PostgreSQL.postgre_sql_connection import db_session


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

def insert_hostage_email_reference(email_id):
    new_hostage_reference = HostageModel(
        email_id=email_id
    )

    db_session.add(new_hostage_reference)
    db_session.commit()

    return new_hostage_reference.id

def insert_explos_email_reference(email_id):
    new_explos_reference = ExplosModel(
        email_id=email_id
    )

    db_session.add(new_explos_reference)
    db_session.commit()

    return new_explos_reference.id