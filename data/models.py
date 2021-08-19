from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import Table

from .enums import TypeEnum, MuscleEnum, EquipmentEnum
from .database import Base

class Alternative(Base):
    __tablename__ = "alternatives"

    exercise_id = Column("exerciseId", Integer, ForeignKey("exercises.id"), primary_key=True)
    alternative_id = Column("alternativeId", Integer, ForeignKey("exercises.id"), primary_key=True)

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    instructions = Column(String, default="")

    details = relationship("Detail", backref="details")
    media = relationship("Media", backref="media")
    alternatives = relationship("Exercise",
                                secondary="alternatives",
                                primaryjoin=id==Alternative.exercise_id,
                                secondaryjoin=id==Alternative.alternative_id)

class Detail(Base):
    __tablename__ = "details"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(Enum(TypeEnum))
    main_muscle = Column(Enum(MuscleEnum))
    equipment = Column(Enum(EquipmentEnum))
    
    exercise_id = Column(Integer, ForeignKey("exercises.id"))

class Media(Base):
    __tablename__ = "media"

    id = Column(Integer, primary_key=True, index=True)
    figure_img = Column(String)
    figure_url = Column(String)
    video = Column(String)

    exercise_id = Column(Integer, ForeignKey("exercises.id"))


