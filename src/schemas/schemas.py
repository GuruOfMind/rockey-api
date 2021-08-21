from __future__ import annotations
from typing import List, Optional
from src.utils.enums import TypeEnum, MuscleEnum, EquipmentEnum

from pydantic import BaseModel

class Exercise(BaseModel):
    id: int
    name: str
    instructions: Optional[str] = ""
    video: str
    details: ExerciseDetail
    media: List[ExerciseMedia] = []

    alternatives: Optional[List[int]] = []

    class Config:
        orm_mode = True

class ExerciseDetail(BaseModel):
    type: TypeEnum = TypeEnum.Strongman
    main_muscle: MuscleEnum = MuscleEnum.Chest
    equipment: EquipmentEnum = EquipmentEnum.Other
    
    class Config:
        orm_mode = True

class ExerciseMedia(BaseModel):
    figure_img: str
    figure_url: str
    
    class Config:
        orm_mode = True

class ExerciseAlternative(BaseModel):
    alternative_id: Optional[int] = None
    
    class Config:
        orm_mode = True

class ExerciseCreate(BaseModel):
    id: int
    name: str
    instructions: Optional[str] = ""
    video: str

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
    alternative_id: int
    
    class Config:
        orm_mode = True

Exercise.update_forward_refs()