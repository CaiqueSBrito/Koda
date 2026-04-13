from fastapi import APIRouter, Depends
from app.schemas.user_schemas import UserResponse
from app.security.rbac import RoleChecker

allow_admin = RoleChecker(["admin"])

router = APIRouter(
    prefix="/api/admin", 
    tags=["Admin"],
    dependencies=[Depends(allow_admin)]
)

@router.get("/", response_model=UserResponse)
async def admin_dashboard(current_admin = Depends(allow_admin)):
    return current_admin