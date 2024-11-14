from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from database.PostgreSQL.models import  *

# TODO: change to the docker port
DB_URL = "postgresql://postgres:12345678@localhost/danger_email"
engine = create_engine(DB_URL)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

def init_db():
    import database.PostgreSQL.models
    Base.metadata.create_all(bind=engine)
