from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .settings import (DATA_BASE_URL, BASE_DIR, os, STAICS_ENDPOINT, uuid)

engine = create_engine(DATA_BASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()