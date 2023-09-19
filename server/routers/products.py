from pydantic import BaseModel
from fastapi import APIRouter, Depends

from functions.jwt_funcs import jwt_bearer
from functions.db_products_funcs import (
    get_product,
    get_all_products
)



router = APIRouter()


@router.get("/get_all_products", tags=["products"])
async def get_all_products_info(user = Depends(jwt_bearer)):
    return get_all_products()

@router.get("/get_product", tags=["products"])
async def get_one_product(user = Depends(jwt_bearer), id: int = 1):
    return get_product(id)