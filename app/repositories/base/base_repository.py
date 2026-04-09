from typing import TypeVar, Generic, List, Optional, Type
from sqlalchemy.orm import Session
from pydantic import BaseModel

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseRepository(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType], db: Session):
        self.model = model
        self.db = db

    def get_all(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        self.db.query(self.model).skip(skip).limit(limit).all()
    
    def get_id(self, model_id: int) -> Optional[ModelType]:
        self.db.query(self.model).filter(self.model.id == model_id).first()
    
    def create(self, data: CreateSchemaType) -> ModelType:
        obj = self.model(**data.model_dump())
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def update(self, db_obj: ModelType, data: UpdateSchemaType) -> ModelType:
        update_data = data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_obj, field, value)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, db_obj: ModelType) -> None:
        self.db.delete(db_obj)
        self.db.commit()