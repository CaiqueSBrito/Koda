from abc import ABC, abstractmethod
from typing import TypeVar, Generic, List, Optional, Type
from pydantic import BaseModel
from app.repositories.contracts.i_base_repository import IBaseRepository
from app.models.services import Service
from app.schemas.services_schemas import ServicesCreate, ServicesUpdate

@abstractmethod
class IServiceRepository(IBaseRepository[Services, ServicesCreate, ServicesUpdate], ABC):
    pass
