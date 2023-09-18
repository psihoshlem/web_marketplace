from pydantic import BaseModel
from fastapi import APIRouter, Depends, Body

from functions.jwt_funcs import jwt_bearer, encodeJWT
from functions.db_user_funcs import (
    create_user,
    auth_user,
    get_user_info_from_db
)

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


@router.get("/get_user_info")
async def get_user_info(user = Depends(jwt_bearer), login = "me"):
    if login == "me":
        login = user
    info = get_user_info_from_db(login)
    return info