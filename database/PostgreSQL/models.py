from sqlalchemy import String, Column, Integer, Date, Table, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class EmailsModel(Base):
    __tablename__ = 'emails'

    emails_id = Column(Integer, primary_key=True) # PK
    country_name = Column(String)

    hostages = relationship('HostageModel', back_populates='email')
    explos = relationship('ExplosModel', back_populates='email')

class HostageModel(Base):
    __tablename__ = 'hostages'

    hostage_id = Column(Integer, primary_key=True) # PK int
    email_id = Column(Integer, ForeignKey("emails.emails_id"))

    email = relationship("EmailsModel", back_populates="hostages")

class ExplosModel(Base):
    __tablename__ = 'explos'

    explos_id = Column(Integer, primary_key=True) # PK int
    email_id = Column(Integer, ForeignKey("emails.emails_id"))

    email = relationship("EmailsModel", back_populates="explos")

