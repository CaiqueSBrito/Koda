from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.repositories.user_repository import UserRepository
from app.services.auth_service import AuthService
from app.schemas.auth_schemas import LoginRequest, TokenResponse, RefreshRequest

router = APIRouter(prefix="api/auth", tags=["Auth"])

def get_auth_service(session: AsyncSession = Depends(get_session)) -> AuthService:
    return AuthService(UserRepository(session))

@router.post("/login", response_model=TokenResponse)
async def login(body: LoginRequest, service: AuthService = Depends(get_auth_service)):
    return await service.login(body)

@router.post("/refresh", response_model=TokenResponse)
async def refresh(body: RefreshRequest, service: AuthService = Depends(get_auth_service)):
    return await service.refresh(body.refresh_token)