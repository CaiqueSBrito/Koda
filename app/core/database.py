from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

engine = create_engine(
    settings.database_url,
    pool_pre_ping=True,     # verifica conexão antes de usar
    pool_size=10,           # conexões simultâneas no pool
    max_overflow=20,        # conexões extras além do pool
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# Dependency para obter sessão do banco
def get_db():
    db = SessionLocal()  
    try:
        yield db
    finally:
        db.close()
