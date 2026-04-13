from fastapi import APIRouter, Depends, status, Query
from typing import List

from app.schemas.user_schemas import UserCreate, UserUpdate, UserResponse
from app.services.contracts.i_user_service import IUserService
from app.core.deps import get_user_service

router = APIRouter()

@router.post("/api", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(
    user_in: UserCreate, 
    service: IUserService = Depends(get_user_service)
):
    """
    Create new user.
    """
    return service.create(user_in)

@router.get("/api", response_model=List[UserResponse], status_code=status.HTTP_200_OK)
def get_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    service: IUserService = Depends(get_user_service)
):
    """
    Retrieve users with pagination.
    """
    return service.get_all(skip=skip, limit=limit)

@router.get("/api/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def get_user(
    user_id: int, 
    service: IUserService = Depends(get_user_service)
):
    """
    Get a specific user by id.
    """
    return service.get_by_id(user_id)

@router.put("/api/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
def update_user(
    user_id: int, 
    user_in: UserUpdate, 
    service: IUserService = Depends(get_user_service)
):
    """
    Update a user.
    """
    return service.update(user_id, user_in)

@router.delete("/api/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int, 
    service: IUserService = Depends(get_user_service)
):
    """
    Delete a user.
    """
    service.delete(user_id)
