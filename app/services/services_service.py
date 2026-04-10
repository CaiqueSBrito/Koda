from app.repositories.services_repository import ServiceRepository
from app.schemas.services_schemas import ServicesCreate, ServicesUpdate
from app.models.services import Services
from app.services.base.base_service import BaseService
from app.services.contracts.i_services_service import IServicesService
from typing import List

class ServicesService(BaseService[Services, ServicesCreate, ServicesUpdate], IServicesService):
    def __init__(self, repo: ServiceRepository):
        super().__init__(repo)