from database.PostgreSQL.models import EmailsModel
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