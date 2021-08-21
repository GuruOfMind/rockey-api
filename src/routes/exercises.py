from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src import config
from src.schemas import schemas
from src.api import crud
from src.database import database
from src.utils import enums

router = APIRouter(
    prefix="/api",
    tags=["Exercises"],
)

@router.get("/exercises", response_model=List[schemas.Exercise])
async def get_exercises(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    exercises = crud.get_exercises(db, skip=skip, limit=limit)
    return exercises

@router.post("/exercises", response_model=schemas.ExerciseCreate)
async def create_exercise(exercise: schemas.ExerciseCreate, db: Session = Depends(database.get_db)):
    return crud.add_exercise(db=db, exercise=exercise)

@router.get("/exercises/{exercise_id}", response_model=schemas.Exercise)
async def get_exercise(exercise_id: int, db: Session = Depends(database.get_db)):
    response = crud.get_exercise(db=db, exercise_id=exercise_id)
    
    if response is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return response

@router.get("/types/{exercise_type}", response_model=List[schemas.Exercise])
async def get_exercises_by_type(exercise_type: enums.TypeEnum, db: Session = Depends(database.get_db)):
    response = crud.get_exercises_by_type(db=db, exercise_type=exercise_type)
    
    if response is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return response


@router.get("/muscles/{exercise_muscle}", response_model=List[schemas.Exercise])
async def get_exercises_by_muscle(exercise_muscle: enums.MuscleEnum, db: Session = Depends(database.get_db)):
    response = crud.get_exercises_by_muscle(db=db, exercise_muscle=exercise_muscle)
    
    if response is None:
        raise HTTPException(status_code=404, detail="Exercise not found")
    return response

@router.get("/equipment/{exercise_equipment}", response_model=List[schemas.Exercise])
async def get_exercises_by_equipment(exercise_equipment: enums.EquipmentEnum, db: Session = Depends(database.get_db)):
    response = crud.get_exercises_by_equipment(db=db, exercise_equipment=exercise_equipment)
    
    if response is None:
        raise HTTPException(status_code=404, detail="Equipment not found")
    return response
