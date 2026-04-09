from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional, Type
from app.repositories.contracts.i_base_repository import IBaseRepository
from pydantic import BaseModel

ModelType    = TypeVar("ModelType", bound=BaseModel)
CreateType   = TypeVar("CreateType", bound=BaseModel)
UpdateType   = TypeVar("UpdateType", bound=BaseModel)

@abstractmethod
class IUserRepository(ABC, IBaseRepository):
   
    @abstractmethod
    def get_by_number(self, number: str) -> Optional[ModelType]:
        pass