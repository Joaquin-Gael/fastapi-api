from fastapi import APIRouter, Form, Depends
from fastapi.responses import JSONResponse
from ..settings import OutPutData
from ..models.products import Products, Session
from ..dependencies import products_form, ProductsForm, Optional

products = APIRouter()

@products.get("/productos")
async def get_products():
    with Session() as db:
        products_db = db.query(Products).all()
        products = [product.to_dict() for product in products_db]
        OutPutData(products)
    data = [{"titulo": product.name, "descripcion": product.description, "imagen": product.image, "url": product.url} for product in products_db]
    return data

@products.post("/productos")
async def create_product(product: ProductsForm = Depends(products_form)):
    with Session() as db:
        try:
            product_db = Products(
                name=product.name,
                description=product.description,
                price=product.price,
                image=product.price,
                url_image=product.url_image,
                url=product.url
            )
            db.add(product_db)
            db.commit()
            return JSONResponse(content={"message": "Producto creado","data": product_db.to_dict()})
        except Exception as e:
            db.rollback()
            return JSONResponse(
                content={"message": "Error creating product"},
                status_code=500
            )