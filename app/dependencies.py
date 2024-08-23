from fastapi.templating import Jinja2Templates
from .settings import (IP_BANED, BASE_DIR, MEDIA_DIR, MEDIA_ENDPOINT, STAICS_DIR, STAICS_ENDPOINT, os, TEMPLATES_DIR)
from fastapi import Depends, Form, Request
from pydantic import BaseModel
from typing  import Optional

templates = Jinja2Templates(directory=TEMPLATES_DIR)

class ProductsForm(BaseModel):
    name: str
    description: str
    price: int
    image: Optional[str] = None
    url_image: Optional[str] = None
    url: str

def products_form(request: Request, name: str = Form(...), description: str = Form(...), price: int = Form(...), image: Optional[str] = Form(None), url_image: Optional[str] = Form(None), url: str = Form(...)) -> ProductsForm:
    return ProductsForm(
        name=name,
        description=description,
        price=price,
        image=image,
        url_image=url_image,
        url=url,
    )