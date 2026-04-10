from sqlalchemy import Column, String, Boolean
from app.core.database import Base
from app.models.timestamp import TimestampMixin

class User(Base, TimestampMixin):
    __tablename__ = "users"

    username   = Column(String(100), nullable=False)
    email  = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    number = Column(String(15), unique=True, nullable=False)