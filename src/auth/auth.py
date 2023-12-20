from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from src.database import SessionLocal, engine
from typing import Annotated
from src.auth.schemas import RegisterUser, Token
from src.auth.models import User
import bcrypt
from src.auth.config import SALT, JWT_ALGORITM, JWT_SECRET
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from datetime import timedelta, datetime
import jwt




router = APIRouter(
    prefix='/auth',
    tags=['auth']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
oauth2 = OAuth2PasswordBearer(tokenUrl='/auth/token')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def register_user(register_user: RegisterUser, db: db_dependency):
    new_user = User(
        email = register_user.email,
        login = register_user.login,
        hashed_password = bcrypt.hashpw(register_user.password.encode(), str(SALT).encode()).decode()    
    )
    db.add(new_user)
    db.commit()


@router.post('/token', response_model=Token)
async def login_fot_acces_token(db: db_dependency,
                                form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user.1')
    token = create_access_token(user.login, user.email, timedelta(minutes=30))
    return {'access_token': token, 'token_type': 'bearer'}


    

def authenticate_user(username: str, password: str, db):
    user = db.query(User).filter(User.login == username).first()
    if not user:
        return False
    if not bcrypt.checkpw(password.encode(), user.hashed_password.encode()):
        return False
    return user

def create_access_token(login: str, email: str, expires_delta: timedelta):
    encode = {'sub': login, 'email': email}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, key=JWT_SECRET, algorithm=JWT_ALGORITM)

async def get_current_user(token: Annotated[str, Depends(oauth2)]):
    try: 
        payload = jwt.decode(token, key=JWT_SECRET, algorithms=[JWT_ALGORITM])
        login: str = payload.get('sub')
        email: str = payload.get('email')
        if login is None or email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user2')
        return {'login': login, 'email': email}
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user3')