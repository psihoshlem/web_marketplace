from pydantic import BaseModel
from fastapi import APIRouter, Depends, Body

from functions.jwt_funcs import jwt_bearer
from functions.db_user_funcs import (
    get_user_info_from_db,
    add_friendship,
    get_user_friends
)

class AuthUserSchema(BaseModel):
    login: str 
    password: str


router = APIRouter()

@router.get("/get_user_info", tags=["users"])
async def get_user_info(user = Depends(jwt_bearer), login = "me"):
    if login == "me":
        login = user
    info = get_user_info_from_db(login)
    return info

@router.post("/add_friend", tags=["users"])
async def add_friend(login, user = Depends(jwt_bearer)):
    add_friendship(user, login)
    return "Success"

@router.get("/get_friends", tags=["users"])
async def get_user_info(user = Depends(jwt_bearer), login = "me"):
    if login == "me":
        login = user
    return get_user_friends(login)


# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpbiI6InNlbmtzIn0.9DN3EgTJRoXrkcYiCCJX6EImw5iRYMcXCMldfMQt0BM