from fastapi import HTTPException, status, Depends
from app.core.deps import get_current_user
# Aqui você importaria seu modelo de User real para a tipagem, ex: from app.models.user import User
from app.models.user import User

class RoleChecker:
    def __init__(self, allowed_roles: list[str]):
        self.allowed_roles = allowed_roles

    def __call__(self, current_user: User = Depends(get_current_user)):
        if not hasattr(current_user, "role") or current_user.role not in self.allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Sem permissão para acessar este recurso"
            )
        return current_user