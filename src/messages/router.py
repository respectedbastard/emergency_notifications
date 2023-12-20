from fastapi import APIRouter, Depends, File
from src.messages.schemas import CreateContact
from src.auth.auth import get_current_user
from typing import Annotated
from src.database import SessionLocal, Base, engine
from sqlalchemy.orm import Session
from src.messages.models import Contact
from src.auth.models import User


message_router = APIRouter(
    prefix='/message',
    tags=['message']
)

user_dependency = Annotated[dict, Depends(get_current_user)]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
db_dependency = Annotated[Session, Depends(get_db)]


async def get_contact(db: db_dependency, user: user_dependency):
    user_login = user.get('login')
    user_contacts = db.query(User).get(user_login)
    contacts = user_contacts.contacts_rel

    return contacts
user_contacts_dependency = Annotated[dict, Depends(get_contact)]



@message_router.post('/add_contact')
async def add_contact(new_contact: CreateContact, user: user_dependency, db: db_dependency):
    contact = Contact(contact_email = new_contact.contact_email, 
                      contact_name = new_contact.contact_name,
                      user_login = user.get('login'))
    db.add(contact)
    db.commit()

    return {'ec':'gtiyj'}

@message_router.get('/my_contacts')
async def get_my_contacts(contacts: user_contacts_dependency):
    return {'ans':contacts}

@message_router.post('/add_contacts')
async def add_contacts(contacts: Annotated[bytes, File()], user: user_dependency):
    if not contacts:
        return {'No contatcs': 'added'}
    else:
        return {'file': len(contacts)}

