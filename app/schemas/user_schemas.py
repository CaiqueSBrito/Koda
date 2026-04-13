from pydantic import BaseModel, EmailStr, Field
from datetime import datetime
from typing import Optional

# Base compartilhada entre schemas
class UserBase(BaseModel):
    username: str = Field(..., min_length=2, max_length=100)
    email: EmailStr
    number: str = Field(..., min_length=11, max_length=11)
''
# Dados para criação (POST)
class UserCreate(UserBase):
    password: str
    @field_validator("password")
    @classmethod
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError("Senha deve ter no mínimo 8 caracteres")
        if not any(c.isupper() for c in v):
            raise ValueError("Senha deve conter ao menos uma letra maiúscula")
        if not any(c.isdigit() for c in v):
            raise ValueError("Senha deve conter ao menos um número")
        return v
        
    pass

# Dados para atualização parcial (PUT)
class UserUpdate(BaseModel):
    username: Optional[str] = Field(None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None

# Resposta da API (GET/POST/PUT)
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True  # Pydantic v2: lê atributos de objetos ORM