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
    data = [{"titulo": product.name, "descripcion": product.description, "imagen": product.url_image, "url": product.url} for product in products_db]
    return data

@products.post("/productos")
async def create_product(product: ProductsForm = Depends(products_form)):
    with Session() as db:
        try:
            print(product)
            product_db = Products(
                name=product.name,
                description=product.description,
                price=product.price,
                image="None" if product.image is None else product.image.filename,
                url_image=product.url_image,
                url=product.url
            )
            if product.image is not None:
                product_db.upload_image(product.image)
            db.add(product_db)
            db.commit()
            return JSONResponse(content={"message": "Producto creado","data": product_db.to_dict()})
        except Exception as e:
            print(e)
            db.rollback()
            return JSONResponse(
                content={"message": "Error creating product"},
                status_code=500
            )