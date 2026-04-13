from abc import ABC, abstractmethod
from app.schemas.auth_schemas import LoginRequest, TokenResponse

class IAuthService(ABC):
    @abstractmethod
    async def login(self, data: LoginRequest) -> TokenResponse: 
        pass

    @abstractmethod
    async def refresh(self, refresh_token: str) -> TokenResponse: 
        pass