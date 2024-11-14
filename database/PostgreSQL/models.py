from sqlalchemy import String, Column, Integer, ForeignKey, JSON
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class EmailsModel(Base):
    __tablename__ = 'emails'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    ip_address = Column(String)
    created_at = Column(String)
    location = Column(JSON)
    device_info = Column(JSON)
    sentences = Column(JSON)

    hostages = relationship('HostageModel', back_populates='email')
    explos = relationship('ExplosModel', back_populates='email')

class HostageModel(Base):
    __tablename__ = 'hostages'

    id = Column(Integer, primary_key=True) # PK int
    email_id = Column(Integer, ForeignKey("emails.id"))

    email = relationship("EmailsModel", back_populates="hostages")

class ExplosModel(Base):
    __tablename__ = 'explos'

    id = Column(Integer, primary_key=True) # PK int
    email_id = Column(Integer, ForeignKey("emails.id"))

    email = relationship("EmailsModel", back_populates="explos")

