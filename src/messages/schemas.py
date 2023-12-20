from pydantic import BaseModel, EmailStr



class CreateContact(BaseModel):
    contact_name: str
    contact_email: EmailStr