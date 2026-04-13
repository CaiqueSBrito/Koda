from fastapi import APIRouter, Depends, status, Query
from typing import List

from app.schemas.services_schemas import ServicesResponse, ServicesCreate, ServicesUpdate
from app.services.contracts.i_services_service import IServicesService
from app.core.deps import get_services_service

router = APIRouter()

@router.post("/api", response_model=ServicesResponse, status_code=status.HTTP_201_CREATED)
def create_service(
    service_in: ServicesCreate,
    service: IServicesService = Depends(get_services_service)
):
    return service.create(service_in)

@router.get("/api", response_model=List[ServicesResponse])
def get_services(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    service: IServicesService = Depends(get_services_service)
):
    return service.get_all(skip=skip, limit=limit)

@router.get("/api/avaliable", response_model=List[ServicesResponse])
def get_avaliable_services(
    service: IServicesService = Depends(get_services_service)
):
    return service.get_avaliable()

@router.get("/api/{service_id}", response_model=ServicesResponse)
def get_service(
    service_id: int,
    service: IServicesService = Depends(get_services_service)
):
    return service.get_by_id(service_id)

@router.put("/api/{service_id}", response_model=ServicesResponse)
def update_service(
    service_id: int,
    service_in: ServicesUpdate,
    service: IServicesService = Depends(get_services_service)
):
    return service.update(service_id, service_in)

@router.delete("/api/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service(
    service_id: int,
    service: IServicesService = Depends(get_services_service)
):
    service.delete(service_id)