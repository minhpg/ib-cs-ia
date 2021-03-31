from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from models import user as userModel

router = APIRouter(
 prefix="/auth",   
)

class User(BaseModel):
    username: str
    email: EmailStr
    password: str

@router.post('/login')
async def login(user: User):
    pass

@router.post('/create')
async def create(user: User):
    pass
    
