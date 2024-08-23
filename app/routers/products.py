from fastapi import APIRouter
from fastapi.responses import JSONResponse
from ..settings import OutPutData

products = APIRouter()

@products.get("/productos")
async def get_products():
    return [
        {"titulo": "Producto 1", "descripcion": "Descripción del producto 1", "imagen": "img1.jpg", "url": "/producto/1"},
        {"titulo": "Producto 2", "descripcion": "Descripción del producto 2", "imagen": "img2.jpg", "url": "/producto/2"},
        {"titulo": "Producto 3", "descripcion": "Descripción del producto 3", "imagen": "img3.jpg", "url": "/producto/3"}
    ]