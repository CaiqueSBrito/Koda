from fastapi import HTTPException, status
from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreate, UserUpdate
from app.models.user import User
from app.services.base.base_service import BaseService

class UserService(BaseService[User, UserCreate, UserUpdate]):
    def __init__(self, repo: UserRepository):
        super().__init__(repo)
        self.repo = repo

    def create(self, data: UserCreate) -> User:
        if hasattr(data, "email") and self.repo.get_by_email(data.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email já cadastrado"
            )
        return super().create(data)
