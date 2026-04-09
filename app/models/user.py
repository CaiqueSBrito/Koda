from sqlalchemy import Column, String
from app.core.database import Base
from app.models.timestamp import TimestampMixin

class User(Base, TimestampMixin):
    __tablename__ = "users"

    name   = Column(String(100), nullable=False)
    number = Column(String(15), unique=True, nullable=False)