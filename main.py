
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()

# Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


@app.get("/")
def home():
    response = {
        "error":{
            "message": "This API is for Exercises data"
        }
    }
    return JSONResponse(content=response)

# @app.get("/exercises", response_model=List[schemas.Exercise])
# async def get_exercises(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     exercises = crud.get_exercises(db, skip=skip, limit=limit)
#     return exercises

# @app.post("/exercises", response_model=schemas.ExerciseCreate)
# async def create_exercise(exercise: schemas.ExerciseCreate, db: Session = Depends(get_db)):
#     return crud.add_exercise(db=db, exercise=exercise)

# @app.get("/exercises/{exercise_id}", response_model=schemas.Exercise)
# async def get_exercise(exercise_id: int, db: Session = Depends(get_db)):
#     response = crud.get_exercise(db=db, exercise_id=exercise_id)
    
#     if response is None:
#         raise HTTPException(status_code=404, detail="Exercise not found")
#     return response

# @app.get("/types/{exercise_type}", response_model=List[schemas.Exercise])
# async def get_exercises_by_type(exercise_type: enums.TypeEnum, db: Session = Depends(get_db)):
#     response = crud.get_exercises_by_type(db=db, exercise_type=exercise_type)
    
#     if response is None:
#         raise HTTPException(status_code=404, detail="Exercise not found")
#     return response


# @app.get("/muscles/{exercise_muscle}", response_model=List[schemas.Exercise])
# async def get_exercises_by_muscle(exercise_muscle: enums.MuscleEnum, db: Session = Depends(get_db)):
#     response = crud.get_exercises_by_muscle(db=db, exercise_muscle=exercise_muscle)
    
#     if response is None:
#         raise HTTPException(status_code=404, detail="Exercise not found")
#     return response

# @app.get("/equipment/{exercise_equipment}", response_model=List[schemas.Exercise])
# async def get_exercises_by_equipment(exercise_equipment: enums.EquipmentEnum, db: Session = Depends(get_db)):
#     response = crud.get_exercises_by_equipment(db=db, exercise_equipment=exercise_equipment)
    
#     if response is None:
#         raise HTTPException(status_code=404, detail="Equipment not found")
#     return response
