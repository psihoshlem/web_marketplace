from pydantic import BaseModel
from fastapi import APIRouter, Depends, Body

from functions.jwt_funcs import jwt_bearer, encodeJWT
from functions.db_user_funcs import create_user, auth_user

class AuthUserSchema(BaseModel):
    login: str 
    password: str


router = APIRouter()

@router.post("/login")
async def login(user: AuthUserSchema):
    if not auth_user(user.login, user.password):
        return "Non authorized"
    return encodeJWT(user.login)


@router.post("/signup")
async def signup(user: AuthUserSchema):
    if not create_user(user.login, user.password):
        return "Already Exist"
    return encodeJWT(user.login)


@router.get("/getuser")
async def get_user(user = Depends(jwt_bearer)):
    print(user)
    return user