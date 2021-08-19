from typing import List, Optional
from .enums import TypeEnum, MuscleEnum, EquipmentEnum

from pydantic import BaseModel

class Detail(BaseModel):
    id: int
    type: TypeEnum = TypeEnum.Strongman
    main_muscle: MuscleEnum = MuscleEnum.Chest
    equipment: EquipmentEnum = EquipmentEnum.Other

    class Config:
        orm_mode = True

class Figure(BaseModel):
    id: int
    figure_img: str
    figure_url: str

    class Config:
        orm_mode = True

class Exercise(BaseModel):
    id: int
    name: str
    video: str
    intstructions: Optional[str] = ""

    details: Detail
    figure: List[Figure] = []

    class Config:
        orm_mode = True