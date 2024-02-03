import os

from dotenv import load_dotenv

from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy.orm import sessionmaker, declarative_base
from starlette import status


load_dotenv()

username = os.environ.get("USER")
password = os.environ.get("PASSWORD")
db_name = os.environ.get("DB_NAME")
domain = os.environ.get("DOMAIN")

url = f"postgresql+psycopg2://{username}:{password}@{domain}:5432/{db_name}"
Base = declarative_base()
engine = create_engine(url, echo=False, pool_size=5)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


# Dependency
async def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))
    finally:
        db.close()
