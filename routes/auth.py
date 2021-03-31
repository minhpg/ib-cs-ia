from fastapi import APIRouter, HTTPException, Depends, Request
from pydantic import BaseModel, EmailStr
from models import user as userModel
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from .. import auth, db

router = APIRouter(
 prefix="/auth",   
)

class User(BaseModel):
    username: str
    password: str


@AuthJWT.load_config
def get_config():
    return auth.Settings()

@router.exception_handler(AuthJWTException)
def authExceptionHandler(request: Request, exc: AuthJWTException):
    return {"message" : exc.message }

@router.post('/login')
async def login(user: User):
    pass

@router.post('/create')
async def create(user: User):
    db.User(
        username = user.username,
        password = user.password
    ).save()


    
