from abc import ABC, abstractmethod
from app.services.contracts.i_base_service import IBaseService
from app.models.user import User
from app.schemas.user_schemas import UserCreate, UserUpdate

class IUserService(IBaseService[User, UserCreate, UserUpdate], ABC):
    @abstractmethod
    def get_by_number(self, number: str) -> User:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass
