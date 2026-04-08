from fastapi import HTTPException, status
from typing import List
from app.repositories.user_repository import UserRepository
from app.schemas.user_schemas import UserCreate, UserUpdate, UserResponse

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def get_all(self, skip: int, limit: int) -> List[UserResponse]:
        return self.repo.get_all(skip=skip, limit=limit)

    def get_by_id(self, user_id: int) -> UserResponse:
        user = self.repo.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Usuário {user_id} não encontrado"
            )
        return user

    def create(self, data: UserCreate) -> UserResponse:
        if self.repo.get_by_email(data.email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email já cadastrado"
            )
        return self.repo.create(data)

    def update(self, user_id: int, data: UserUpdate) -> UserResponse:
        user = self.get_by_id(user_id)  # já lança 404 se não achar
        if data.email and data.email != user.email:
            if self.repo.get_by_email(data.email):
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Email já está em uso"
                )
        return self.repo.update(user, data)

    def delete(self, user_id: int) -> None:
        user = self.get_by_id(user_id)
        self.repo.delete(user)
