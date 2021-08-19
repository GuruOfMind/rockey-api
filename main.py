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
    return crud.create_exercise(db=db, exercise=exercise)

# @app.post("/exercises")
# async def post_exercise(exercise: Exercise):
#     return exercise

# @app.get("/exercises/{exercise_id}")
# async def get_exercises_by_id(exercise_id: int):
#     response = f"exercise By ID {exercise_id}"
#     # exercise = Exercise({"name": "something"})
#     return {response}