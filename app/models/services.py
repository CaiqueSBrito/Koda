from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Services(Base):
    __tablename__ = "services"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String(40), nullable=False)
    duration    = Column(Integer, nullable=False)
    created_at  = Column(DateTime(timezone=True), server_default=func.now())
    updated_at  = Column(DateTime(timezone=True), onupdate=func.now())