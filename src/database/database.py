import os
from src.config import BASE_DIR
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "resources", "exercises.db")

engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False} 
)

# engine["SQLALCHEMY_ECHO"] = True

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()