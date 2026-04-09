from fastapi import APIRouter, Depends, status, Query
from typing import List

from app.schemas.services_schemas import ServicesResponse, ServicesCreate, ServicesUpdate
from app.services.services_service import ServicesService
from app.core.deps import get_services_service

router = APIRouter()

@router.post("/", response_model=ServicesResponse, status_code=status.HTTP_201_CREATED)
def create_service(
    service_in: ServicesCreate,
    service: ServicesService = Depends(get_services_service)
):
    return service.create(service_in)

@router.get("/", response_model=List[ServicesResponse])
def get_services(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    service: ServicesService = Depends(get_services_service)
):
    return service.get_all(skip=skip, limit=limit)

@router.get("/avaliable", response_model=List[ServicesResponse])
def get_avaliable_services(
    service: ServicesService = Depends(get_services_service)
):
    return service.get_avaliable()

@router.get("/{service_id}", response_model=ServicesResponse)
def get_service(
    service_id: int,
    service: ServicesService = Depends(get_services_service)
):
    return service.get_by_id(service_id)

@router.put("/{service_id}", response_model=ServicesResponse)
def update_service(
    service_id: int,
    service_in: ServicesUpdate,
    service: ServicesService = Depends(get_services_service)
):
    return service.update(service_id, service_in)

@router.delete("/{service_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_service(
    service_id: int,
    service: ServicesService = Depends(get_services_service)
):
    service.delete(service_id)