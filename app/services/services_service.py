from app.repositories.services_repository import ServiceRepository
from app.schemas.services_schemas import ServicesCreate, ServicesUpdate
from app.models.services import Services
from app.services.base.base_service import BaseService

class ServicesService(BaseService[Services, ServicesCreate, ServicesUpdate]):
    def __init__(self, repo: ServiceRepository):
        super().__init__(repo)
