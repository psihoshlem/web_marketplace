from pydantic import BaseModel
from fastapi import APIRouter, Depends, Body

from functions.jwt_funcs import jwt_bearer

class AuthUserSchema(BaseModel):
    login: str 
    password: str

class dataschema(BaseModel):
    adat: str

users = []

router = APIRouter()

@router.post("/login")
async def login(user: AuthUserSchema):
    pass
# return jwt token

@router.post("/signup")
async def signup(user: AuthUserSchema):
    pass
# return jwt token

@router.get("/my_account")
async def my_account(user = Depends(jwt_bearer)):
    
    return user