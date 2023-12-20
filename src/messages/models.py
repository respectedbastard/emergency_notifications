from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from src.database import Base



class Contact(Base):
    __tablename__ = 'contacts'
    contact_email = Column(String, primary_key=True, nullable=False)
    user_login = Column(String, ForeignKey('users.login'), index=True)
    contact_name = Column(String)
    user = relationship('User', backref='contacts_rel')
