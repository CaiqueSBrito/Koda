from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List
from pydantic import BaseModel

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class IBaseService(ABC, Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    @abstractmethod
    def get_all(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        pass

    @abstractmethod
    def get_by_id(self, model_id: int) -> ModelType:
        pass

    @abstractmethod
    def create(self, data: CreateSchemaType) -> ModelType:
        pass

    @abstractmethod
    def update(self, model_id: int, data: UpdateSchemaType) -> ModelType:
        pass

    @abstractmethod
    def delete(self, model_id: int) -> None:
        pass
