from sqlalchemy.orm import Session
from typing import List
from app.models.services import Services
from app.schemas.services_schemas import ServicesCreate, ServicesUpdate
from app.repositories.base.base_repository import BaseRepository
from app.repositories.contracts.i_services_repository import IServiceRepository

class ServiceRepository(BaseRepository[Services, ServicesCreate, ServicesUpdate], IServiceRepository):
    def __init__(self, db: Session):
        super().__init__(model=Services, db=db)
