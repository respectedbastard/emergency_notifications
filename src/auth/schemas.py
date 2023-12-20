from pydantic import BaseModel, EmailStr, StringConstraints
from typing_extensions import Annotated


class RegisterUser(BaseModel):
    email: EmailStr
    login: Annotated[str, StringConstraints(strip_whitespace=True, to_lower=True, min_length=4, max_length=20)]
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str