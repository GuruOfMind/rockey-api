from sqlalchemy.orm import Session

from . import models, schemas

def get_exercises(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Exercise).offset(skip).limit(limit).all()