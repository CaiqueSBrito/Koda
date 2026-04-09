from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional, Type
from pydantic import BaseModel
from app.repositories.contracts.i_base_repository import IBaseRepository

ModelType = TypeVar("ModelType", bound=BaseModel)

@abstractmethod
class IServiceRepository(ABC, IBaseRepository):

    @abstractmethod
    def get_avaliable(self, avaliable: bool = True) -> List[ModelType]:
        pass
