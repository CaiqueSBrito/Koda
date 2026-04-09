from sqlalchemy.orm import Session
from typing import Optional
from app.models.user import User
from app.schemas.user_schemas import UserCreate, UserUpdate
from app.repositories.base.base_repository import BaseRepository

class UserRepository(BaseRepository[User, UserCreate, UserUpdate]):
    def __init__(self, db: Session):
        super().__init__(model=User, db=db)

    def get_by_number(self, number: str) -> Optional[User]:
        return self.db.query(User).filter(User.number == number).first()
