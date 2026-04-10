from fastapi import Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.user_repository import UserRepository
from app.repositories.services_repository import ServiceRepository
from app.services.user_service import UserService
from app.services.services_service import ServicesService
from app.services.contracts.i_user_service import IUserService
from app.services.contracts.i_services_service import IServicesService

def get_user_service(db: Session = Depends(get_db)) -> IUserService:
    repo = UserRepository(db)
    return UserService(repo)

def get_services_service(db: Session = Depends(get_db)) -> IServicesService:
    repo = ServiceRepository(db)
    return ServicesService(repo)
