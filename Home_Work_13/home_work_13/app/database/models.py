from sqlalchemy import Column, Integer, String, Date, DateTime, func
from sqlalchemy.orm import declarative_base

# from pydantic_extra_types.phone_numbers import PhoneNumber


Base = declarative_base()


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    surname = Column(String(50))
    email = Column(String(50))
    phone = Column(String(50))
    description = Column(String(250))
    birth_date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=8000)
    pass
