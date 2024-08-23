from ..database import Base, Session
from sqlalchemy import (Column, Integer, String)

class CustomProductsBase(Base):
    __abstract__ = True

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Products(CustomProductsBase):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    image = Column(String)
    url_image = Column(String)
    url = Column(String)
    