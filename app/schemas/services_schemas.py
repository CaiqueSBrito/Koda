from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class ServicesBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=40)
    duration: int = Field(..., ge=1, le=1440)
    price: float = Field(..., ge=0.0)

class ServicesCreate(ServicesBase):
    pass

class ServicesUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=40)
    duration: Optional[int] = Field(None, ge=1, le=1440)
    price: Optional[float] = Field(None, ge=0.0)

class ServicesResponse(ServicesBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True