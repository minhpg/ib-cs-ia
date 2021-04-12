from fastapi import APIRouter, HTTPException, Depends, Request
from pydantic import BaseModel, EmailStr
from app.models import user as userModel
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
    return {'message' : 'successful', 'data' : response }

@router.post('/login')
async def login(user: User, Authorize: AuthJWT = Depends()):
    data = db.User.objects(user.username)
    if len(data) > 0:
        if data[0].password == user.password:
            access_token = Authorize.create_access_token(subject=data[0].user_id)
            return {"access_token": access_token}
        raise HTTPException(status_code=403,detail='invalid password')
    raise HTTPException(status_code=403,detail='invalid username')
        

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




    
