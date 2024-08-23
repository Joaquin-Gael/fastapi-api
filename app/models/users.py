from sqlalchemy import (Column, Integer, String)
from ..database import Base, Session
from ..settings import (BASE_DIR, os, uuid, MEDIA_ENDPOINT)

class CustomUserBase(Base):
    __abstract__ = True

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    
    def upload_image(self, image_file, upload_dir="users"):
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

class User(CustomUserBase):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    image = Column(String)
    url_image = Column(String)