from sqlalchemy.orm import Session

from . import models, schemas, enums

'''
    Create Objects
'''
def add_exercise(db: Session, exercise: schemas.ExerciseCreate):
    
    db_exercise = models.Exercise(name=exercise.name, instructions=exercise.instructions)
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise

def add_details(db: Session, details: schemas.Detail):
    
    db_details = models.Detail(type=details.type,
                               main_muscle=details.main_muscle,
                               equipment=details.equipment,
                               exercise_id=details.exercise_id)
    db.add(db_details)
    db.commit()
    db.refresh(db_details)
    return db_details

def add_media(db: Session, media: schemas.Media):
    
    db_media = models.Media(figure_img=media.figure_img,
                            figure_url=media.figure_url,
                            video=media.video,
                            exercise_id=media.exercise_id)
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return db_media

def add_alternative(db: Session, alternative: schemas.Alternative):
    alternative_info = db.query(models.Exercise).filter(models.Exercise.name == alternative.alternative_name).first()
    if(alternative_info == None):
        alternative_id = 0
    else:
        alternative_id=alternative_info.id
    db_alternative = models.Alternative(exercise_id=alternative.exercise_id, alternative_id=alternative_id)
    db.add(db_alternative)
    db.commit()
    db.refresh(db_alternative)
    return db_alternative

'''
    Read Objects
'''
def get_exercise(db: Session, exercise_id: int):
    exercise_info = db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()
    return exercise_info

def get_exercise_id(db: Session, exercise_name: str):
    response = db.query(models.Exercise).filter(models.Exercise.name == exercise_name).first()
    return response.id

def get_exercises(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Exercise).offset(skip).limit(limit).all()

def get_exercises_by_type(db: Session, exercise_type: enums.TypeEnum , skip: int = 0, limit: int = 100):
    type_response = db.query(models.Exercise).\
                    join(models.Detail, models.Exercise.id == models.Detail.exercise_id).\
                    filter(models.Detail.type == exercise_type).\
                    all()
    response = []

    for item in type_response:
        response.append(get_exercise(db=db, exercise_id=item.id))
    return response

def get_exercises_by_muscle(db: Session, exercise_muscle: enums.MuscleEnum, skip: int = 0, limit: int = 100):
    return db.query(models.Exercise).filter(models.Exercise).offset(skip).limit(limit).all()

def get_exercises_by_equipment(db: Session, exercise_equipment: enums.EquipmentEnum, skip: int = 0, limit: int = 100):
    return db.query(models.Exercise).filter(models.Exercise).offset(skip).limit(limit).all()
