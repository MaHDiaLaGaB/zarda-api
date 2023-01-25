from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float


class Base(declarative_base):
    pass


class User(Base):
    __tablename__ = "users"
    number_users = Column(Integer)

    for i in range(number_users):
        username = Column(String)

    balance = Column(Float)
    zarda_name = Column(String)
