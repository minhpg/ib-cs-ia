from fastapi import APIRouter, HTTPException, Depends, Request
from pydantic import BaseModel, EmailStr
from models import user as userModel
import uuid
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

@router.middleware("http")
async def successfulRequest(request: Request, call_next):
    response = await call_next(request)
    return {'message' : 'successful', 'data' : response}

@router.post('/login')
async def login(user: User):
    data = db.User.objects(user.username)
    pass

@router.post('/create')
async def create(user: User):
    user_id = str(uuid.uuid4())
    db.User(
        username = user.username,
        password = user.password,
        user_id = user_id
    ).save()
    return {
        'user_id' : user_id
    }




    
