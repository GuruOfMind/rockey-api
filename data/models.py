from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import MetaData, Table

from .enums import TypeEnum, MuscleEnum, EquipmentEnum
from .database import Base

# class Alternative(Base):
#     __tablename__ = "alternatives"

#     exercise_id = Column("exercise_id", Integer, ForeignKey("exercises.id"))
#     alternative_id = Column("alternative_id", Integer, ForeignKey("exercises.id"))

alternatives = Table("alternatives",
                Base.metadata,
                Column("exercise_id", Integer, ForeignKey("exercises.id")),
                Column("alternative_id", Integer, ForeignKey("exercises.id"))
                )

class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    instructions = Column(String, default="")
    video = Column(String)

    details = relationship("Detail", backref="details")
    media = relationship("Media", backref="media")
    alternative = relationship('Exercise',
                                secondary=alternatives,
                                primaryjoin=(alternatives.c.exercise_id == id),
                                secondaryjoin=(alternatives.c.alternative_id == id),
                                backref=backref("alternatives", lazy="joined"),
                                lazy="joined"
                                ) 
    # def __repr__(self) -> str:
    #     return "<Exercise %r>" % self.name

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

    exercise_id = Column(Integer, ForeignKey("exercises.id"))
