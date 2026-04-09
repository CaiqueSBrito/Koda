from sqlalchemy.orm import Session
from typing import List
from app.models.services import Services
from app.schemas.services_schemas import ServicesCreate, ServicesUpdate
from app.repositories.base.base_repository import BaseRepository

class ServiceRepository(BaseRepository[Services, ServicesCreate, ServicesUpdate]):
    def __init__(self, db: Session):
        super().__init__(model=Services, db=db)

    def get_avaliable(self, avaliable: bool = True) -> List[Services]:
        return self.db.query(Services).filter(Services.avaliable == avaliable).all()
