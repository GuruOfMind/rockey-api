from __future__ import annotations
from typing import List, Optional
from .enums import TypeEnum, MuscleEnum, EquipmentEnum

from pydantic import BaseModel

class Exercise(BaseModel):
    id: int
    name: str
    instructions: Optional[str] = ""

    details: Detail
    figure: List[Media] = []

    alternatives: List[Exercise] = []

    class Config:
        orm_mode = True

class ExerciseCreate(BaseModel):
    id: int
    name: str
    instructions: Optional[str] = ""

    class Config:
        orm_mode = True

class Detail(BaseModel):
    id: int
    type: TypeEnum = TypeEnum.Strongman
    main_muscle: MuscleEnum = MuscleEnum.Chest
    equipment: EquipmentEnum = EquipmentEnum.Other
    exercise_id: int

    class Config:
        orm_mode = True

class Media(BaseModel):
    id: int
    figure_img: str
    figure_url: str
    video: str
    exercise_id: int
    
    class Config:
        orm_mode = True

class Alternative(BaseModel):
    exercise_id: int
    alternative_name: str
    
    class Config:
        orm_mode = True

Exercise.update_forward_refs()