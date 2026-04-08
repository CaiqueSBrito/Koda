from fastapi import FastAPI
from app.core.database import engine, Base
from app.routes import user_router

Base.metadata.create_all(bind=engine)  # cria tabelas se não existirem

app = FastAPI(
    title="FastAPI CRUD",
    version="1.0.0",
    description="API de gerenciamento de usuários",
)

app.include_router(user_router.router, prefix="/users", tags=["users"])