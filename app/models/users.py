from sqlalchemy import (Column, Integer, String)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ..settings import (DATA_BASE_URL, BASE_DIR, os, STAICS_ENDPOINT, uuid)

engine = create_engine(DATA_BASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class CustomBase(Base):
    __abstract__ = True

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def upload_image(self, image_file, upload_dir="users"):
        path = f"{BASE_DIR}/media/{upload_dir}"
        endpoint = f"{STAICS_ENDPOINT}/{upload_dir}"

        if not os.path.exists(path):
            os.makedirs(path)

        image_file.filename = f"{uuid.uuid4().hex}_{image_file.filename.split('.')[0]}.{image_file.filename.split('.')[-1]}"
        self.url_image = f"{endpoint}/{image_file.filename}"
        
        with open(f"{path}/{image_file.filename}", "wb") as f:
            f.write(image_file.file.read())
        
        self.image = f"{upload_dir}/{image_file.filename}"
        return self.image

class User(CustomBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    image = Column(String)
    url_image = Column(String)