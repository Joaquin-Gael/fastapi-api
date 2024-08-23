from ..database import Base, Session
from sqlalchemy import (Column, Integer, String)

class Files(Base):
    __tablename__ = "files"

    id = Column(Integer, primary_key=True)
    filename = Column(String)
    content_type = Column(String)
    size = Column(Integer)
    extencion = Column(String)
    url = Column(String)