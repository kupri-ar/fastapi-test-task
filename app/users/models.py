from sqlalchemy import Column, Integer, String, DateTime, func

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(length=12), index=True)
    name = Column(String(length=50))
    surname = Column(String(length=50))
    patronymic = Column(String(length=50))
    phone_number = Column(String(length=50))
    country = Column(String(length=50))
    email = Column(String, unique=True, index=True)
    date_created = Column(DateTime, default=func.now())
    date_modified = Column(DateTime, default=func.now(), onupdate=func.now())
