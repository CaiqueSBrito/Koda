from fastapi import HTTPException, status
from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreate, UserUpdate
from app.models.user import User
from app.services.base.base_service import BaseService
from app.services.contracts.i_user_service import IUserService
from app.security.security import hash_password

class UserService(BaseService[User, UserCreate, UserUpdate], IUserService):
    def __init__(self, repo: UserRepository):
        super().__init__(repo)
        self.repo = repo

    def create(self, data: UserCreate) -> User:
        data.password = hash_password(data.password)
        if self.repo.get_by_email(data.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email já cadastrado"
            )
        if self.repo.get_by_number(data.number):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Número já cadastrado"
            )
        return super().create(data)
    
    def get_by_number(self, number: str) -> User:
        user = self.repo.get_by_number(number)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuário não encontrado"
            )
        return user
    
    def get_by_email(self, email: str) -> User:
        user = self.repo.get_by_email(email)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuário não encontrado"
            )
        return user