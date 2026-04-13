from typing import TypeVar, Generic, List, Type
from fastapi import HTTPException, status
from pydantic import BaseModel
from sqlalchemy.exc import IntegrityError
from app.repositories.base.base_repository import BaseRepository
from app.services.contracts.i_base_service import IBaseService

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseService(IBaseService[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, repo: BaseRepository[ModelType, CreateSchemaType, UpdateSchemaType]):
        self.repo = repo

    def get_all(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return self.repo.get_all(skip=skip, limit=limit)

    def get_by_id(self, model_id: int) -> ModelType:
        obj = self.repo.get_by_id(model_id)
        if not obj:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Registro com ID {model_id} não encontrado"
            )
        return obj

    def create(self, data: CreateSchemaType) -> ModelType:
        try:
            return self.repo.create(data)
        except IntegrityError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Registro com {data} já existe"
            )

    def update(self, model_id: int, data: UpdateSchemaType) -> ModelType:
        db_obj = self.get_by_id(model_id) 
        return self.repo.update(db_obj, data)

    def delete(self, model_id: int) -> None:
        db_obj = self.get_by_id(model_id)
        self.repo.delete(db_obj)
