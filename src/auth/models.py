from sqlalchemy import  Table, Column, String, Integer, MetaData
from sqlalchemy.orm import relationship
from src.database import Base



class User(Base):
    __tablename__ = 'users'


    email = Column(String, unique=True)
    login = Column(String, primary_key=True, index=True, unique=True)
    hashed_password = Column(String)
    contacts = relationship('Contact', backref='user_rel')
