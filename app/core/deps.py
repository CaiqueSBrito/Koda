from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.user_repository import UserRepository
from app.repositories.services_repository import ServiceRepository
from app.services.user_service import UserService
from app.services.services_service import ServicesService

def get_user_service(db: Session = Depends(get_db)) -> UserService:
    repo = UserRepository(db)
    return UserService(repo)

def get_services_service(db: Session = Depends(get_db)) -> ServicesService:
    repo = ServiceRepository(db)
    return ServicesService(repo)
