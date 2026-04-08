from sqlalchemy.orm import Session
from typing import Optional, List
from app.models.services import Services
from app.schemas.services_schemas import ServicesCreate, ServicesUpdate

class ServiceRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> List[Services]:
        return self.db.query(Services).offset(skip).limit(limit).all()

    def get_by_id (self, services_id) -> Optional[Services]:
        return self.db.query(Services).filter(Services.id == services_id).first()
    
    def create (self, data: ServicesCreate) -> Services:
        services = Services(**data.model_dump())
        self.db.add(services)
        self.db.commit()
        self.db.refresh(services)
        return db

    def update (self, services: Services ,data: ServicesUpdate) -> Services:
        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items:
            setattr(services, fields, value)
        self.db.commit()
        self.db.refresh(services)
        return services

    def exclude (self, services: Services) -> None:
        self.db.delete(services)
        self.db.commit()

        
