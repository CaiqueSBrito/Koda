from sqlalchemy.orm import Session
from typing import Optional
from app.models.user import User
from app.schemas.user_schemas import UserCreate, UserUpdate
from app.repositories.base.base_repository import BaseRepository
from app.repositories.contracts.i_user_repository import IUserRepository

class UserRepository(BaseRepository[User, UserCreate, UserUpdate], IUserRepository):
    def __init__(self, db: Session):
        super().__init__(model=User, db=db)

    def get_by_number(self, number: str) -> Optional[User]:
        return self.db.query(User).filter(User.number == number).first()

    def get_by_email(self, email: str) -> Optional[User]:
        return self.db.query(User).filter(User.email == email).first()
