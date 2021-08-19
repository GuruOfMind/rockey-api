from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Details(BaseModel):
    type: str
    main_muscle: str
    equipment: str

class Images(BaseModel):
    image_1: str
    image_2: str
    image_1_url: str
    image_2_url: str

class Exercise(BaseModel):
    name: str
    details: Details
    video: str
    images: Images
    instructions: Optional[str] = None
    alternative: Optional[list[str]] = None

app = FastAPI()

@app.get("/exercises")
async def get_exercises():
    return {"exercises"}


@app.post("/exercises")
async def post_exercise(exercise: Exercise):
    return exercise

@app.get("/exercises/{exercise_id}")
async def get_exercises_by_id(exercise_id: int):
    response = f"exercise By ID {exercise_id}"
    # exercise = Exercise({"name": "something"})
    return {response}