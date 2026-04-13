from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db, get_session
from app.repositories.user_repository import UserRepository
from app.repositories.services_repository import ServiceRepository
from app.services.user_service import UserService
from app.services.services_service import ServicesService
from app.services.contracts.i_user_service import IUserService
from app.services.contracts.i_services_service import IServicesService
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession
from app.security.security import decode_token

def get_user_service(db: Session = Depends(get_db)) -> IUserService:
    repo = UserRepository(db)
    return UserService(repo)

def get_services_service(db: Session = Depends(get_db)) -> IServicesService:
    repo = ServiceRepository(db)
    return ServicesService(repo)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

async def get_current_user(
    token: str = Depends(oauth2_scheme),
    session: AsyncSession = Depends(get_session)
):
    try:
        payload = decode_token(token)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")

    if payload.get("type") != "access":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Tipo de token inválido")

    user_repo = UserRepository(session)
    user = await user_repo.get_id(payload["sub"])

    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuário não encontrado")
        
    return user

async def get_current_admin_user(current_user = Depends(get_current_user)):
    if not hasattr(current_user, 'role') or current_user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Acesso restrito para administradores")
    return current_user