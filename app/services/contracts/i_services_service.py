from abc import ABC, abstractmethod
from typing import List
from app.services.contracts.i_base_service import IBaseService
from app.models.services import Services
from app.schemas.services_schemas import ServicesCreate, ServicesUpdate

class IServicesService(IBaseService[Services, ServicesCreate, ServicesUpdate], ABC):
    pass