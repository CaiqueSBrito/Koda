from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional
from pydantic import BaseModel

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class IBaseRepository(ABC, Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        pass

    @abstractmethod
    def get_by_id(self, model_id: int) -> Optional[ModelType]:
        pass

    @abstractmethod
    def create(self, data: CreateSchemaType) -> ModelType:
        pass

    @abstractmethod
    def update(self, db_obj: ModelType, data: UpdateSchemaType) -> ModelType:
        pass

    @abstractmethod
    def delete(self, db_obj: ModelType) -> None:
        pass