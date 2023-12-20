from fastapi import FastAPI, Depends
from src.auth.auth import router, get_current_user, db_dependency
from typing import Annotated
from src.messages.router import message_router





app = FastAPI(title='Emergency Notifications')
app.include_router(router)
app.include_router(message_router)

user_dependency = Annotated[dict, Depends(get_current_user)]

@app.get('/')
async def root(user: user_dependency, db: db_dependency):
    return {'success': 'sucsessfull'}

@app.get('/a')
async def root(user: user_dependency, db: db_dependency):
    user_login = user.get('login')
    return {'success': user_login}