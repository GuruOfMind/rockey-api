from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from .enums import TypeEnum, MuscleEnum, EquipmentEnum
from .database import Base


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    video = Column(String)
    instructions = Column(String, default="")

    details = relationship("Detail", back_populates="exercise")
    figures = relationship("Figure")

class Detail(Base):
    __tablename__ = "details"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(TypeEnum))
    main_muscle = Column(Enum(MuscleEnum))
    equipment = Column(Enum(EquipmentEnum))
    
    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    exercise = relationship("Exercise", back_populates="detail")

class Figure(Base):
    __tablename__ = "figures"

    id = Column(Integer, primary_key=True, index=True)
    figure_img = Column(String)
    figure_url = Column(String)

    exercise_id = Column(Integer, ForeignKey("exercises.id"))
    exercise = relationship("Exercise", back_populates="figure")
    # images_id = Column(Integer, ForeignKey("images.id"))

class Alternative(Base):
    __tablename__ = "alternatives"

    exercise_id = Column(Integer, ForeignKey("exercise.id"))
    alternative_exercise = Column(String)