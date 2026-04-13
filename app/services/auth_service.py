from fastapi import HTTPException, status
from app.services.contracts.i_auth_service import IAuthService
from app.repositories.contracts.i_user_repository import IUserRepository
from app.schemas.auth_schemas import LoginRequest, TokenResponse
from app.security.security import verify_password, create_access_token, create_refresh_token, decode_token

class AuthService(IAuthService):
    def __init__(self, user_repository: IUserRepository):
        self._user_repo = user_repository

    async def login(self, data: LoginRequest) -> TokenResponse:
        user = await self._user_repo.find_by_email(data.email)
        if not user or not verify_password(data.password, user.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais inválidas")

        return TokenResponse(
            access_token=create_access_token(str(user.id)),
            refresh_token=create_refresh_token(str(user.id)),
        )

    async def refresh(self, refresh_token: str) -> TokenResponse:
        try:
            payload = decode_token(refresh_token)
        except ValueError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Refresh token inválido")

        if payload.get("type") != "refresh":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Tipo de token inválido")

        return TokenResponse(
            access_token=create_access_token(payload["sub"]),
            refresh_token=create_refresh_token(payload["sub"]),
        )