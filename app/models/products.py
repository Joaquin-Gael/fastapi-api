from ..database import Base, Session
from sqlalchemy import (Column, Integer, String)
from ..settings import (BASE_DIR, os, uuid, MEDIA_ENDPOINT)

class CustomProductsBase(Base):
    __abstract__ = True

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def upload_image(self, image_file, upload_dir="products"):
        path = f"{BASE_DIR}/media/{upload_dir}"
        endpoint = f"{MEDIA_ENDPOINT}{upload_dir}"

        if not os.path.exists(path):
            os.makedirs(path)

        image_file.filename = f"{uuid.uuid4().hex}_{image_file.filename.split('.')[0]}.{image_file.filename.split('.')[-1]}"
        self.url_image = f"{endpoint}/{image_file.filename}"
        
        with open(f"{path}/{image_file.filename}", "wb") as f:
            f.write(image_file.file.read())
        
        self.image = f"{upload_dir}/{image_file.filename}"
        return self.image

class Products(CustomProductsBase):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    image = Column(String)
    url_image = Column(String)
    url = Column(String)
    