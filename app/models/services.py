from sqlalchemy import Column, Integer, String, Boolean
from app.core.database import Base
from app.models.timestamp import TimestampMixin

class Services(Base, TimestampMixin):
    __tablename__ = "services"

    name      = Column(String(40), nullable=False)
    duration  = Column(Integer, nullable=False)