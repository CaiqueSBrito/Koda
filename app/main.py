from fastapi import FastAPI
from app.core.database import engine, Base
from app.routes import user_router
from app.routes import services_router
from app.routes import auth_router
from app.routes import admin_router
from fastapi.middleware.cors import CORSMiddleware
from app.security.middleware import SecurityHeadersMiddleware, limiter
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

Base.metadata.create_all(bind=engine)  # cria tabelas se não existirem

app = FastAPI(
    title="FastAPI CRUD",
    version="1.0.0",
    description="API de gerenciamento de usuários",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SecurityHeadersMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization"],
    allow_credentials=True,
)

app.include_router(auth_router.router, prefix="/api")
app.include_router(user_router.router, prefix="/users", tags=["users"])
app.include_router(services_router.router, prefix="/services", tags=["services"])
app.include_router(admin_router.router)
