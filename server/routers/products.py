from pydantic import BaseModel
from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from functions.jwt_funcs import jwt_bearer
from functions.db_products_funcs import (
    get_product,
    get_all_products,
    get_products
)



router = APIRouter()


@router.get("/get_all_products", tags=["products"])
async def get_all_products_info():
    return get_all_products()

@router.get("/get_product", tags=["products"])
async def get_one_product(user = Depends(jwt_bearer), id: int = 1):
    return get_product(id, user)

@router.get("/search", tags=["products"])
async def search_product(query):
    return get_products(query)

@router.get("/getimage/{filename}")
async def get_image(filename: str):
    image_path = f"./images/{filename}"
    return FileResponse(image_path, media_type="image/jpeg")