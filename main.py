from data import enums
from typing import List, Optional

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm.session import Session

import data.crud as crud
import data.models as models
import data.schemas as schemas
from data.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/exercises", response_model=List[schemas.Exercise])
async def get_exercises(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    exercises = crud.get_exercises(db, skip=skip, limit=limit)
    return exercises

@app.post("/exercises", response_model=schemas.ExerciseCreate)
def create_exercise(exercise: schemas.ExerciseCreate, db: Session = Depends(get_db)):
    return crud.add_exercise(db=db, exercise=exercise)

@app.get("/exercises/{exercise_id}", response_model=schemas.Exercise)
def get_exercise(exercise_id: int, db: Session = Depends(get_db)):
    response = crud.get_exercise(db=db, exercise_id=exercise_id)
    
    if response is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return response

@app.get("/types/{exercise_type}")
def get_exercises_by_type(exercise_type: enums.TypeEnum, db: Session = Depends(get_db)):
    response = crud.get_exercises_by_type(db=db, exercise_type=exercise_type)
    
    if response is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return response
