from abc import ABC, abstractmethod
from typing import Optional
from app.repositories.contracts.i_base_repository import IBaseRepository
from app.models.user import User
from app.schemas.user_schemas import UserCreate, UserUpdate

class IUserRepository(IBaseRepository[User, UserCreate, UserUpdate], ABC):
    @abstractmethod
    def get_by_number(self, number: str) -> Optional[User]:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> Optional[User]:
        pass