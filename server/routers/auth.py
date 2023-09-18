from pydantic import BaseModel
from fastapi import APIRouter

from functions.jwt_funcs import encodeJWT
from functions.db_user_funcs import (
    create_user,
    auth_user,
)

class AuthUserSchema(BaseModel):
    login: str 
    password: str

class RegUserSchema(BaseModel):
    login: str 
    password: str
    address: str
    name: str
    lastname: str
    age: int
    height: float
    weight: float
    personality_type: str

router = APIRouter()

@router.post("/login", tags=["auth"])
async def login(user: AuthUserSchema):
    if not auth_user(user.login, user.password):
        return "Non authorized"
    return encodeJWT(user.login)


@router.post("/signup", tags=["auth"])
async def signup(user: RegUserSchema):
    if not create_user(user):
        return "Already Exist"
    return encodeJWT(user.login)
