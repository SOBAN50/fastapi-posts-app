from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:saeed50ajmal@localhost/fastapi"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# SessionLocal is the thing responsible for talking to database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db(): # For every request to any api endpoint, this will be called, and then closed.
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()