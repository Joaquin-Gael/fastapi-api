from fastapi.templating import Jinja2Templates
from .settings import (IP_BANED, BASE_DIR, MEDIA_DIR, MEDIA_ENDPOINT, STAICS_DIR, STAICS_ENDPOINT, os, TEMPLATES_DIR)
from fastapi import Depends, Form, Request, UploadFile
from pydantic import BaseModel
from typing  import Optional

templates = Jinja2Templates(directory=TEMPLATES_DIR)

class ProductsForm(BaseModel):
    name: str
    description: str
    price: int
    image: Optional[UploadFile] = None
    url_image: Optional[str] = None
    url: Optional[str] = None

def products_form(request: Request,
    name: str = Form(...),
    description: str = Form(...),
    price: int = Form(...),
    image: Optional[UploadFile] = Form(None),
    url_image: Optional[str] = Form(None),
    url: Optional[str] = Form(None)) -> ProductsForm:
    return ProductsForm(
        name=name,
        description=description,
        price=price,
        image=image if image is not None else None,
        url_image=url_image,
        url=url,
    )