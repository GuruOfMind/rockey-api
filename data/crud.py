from sqlalchemy.orm import Session

from . import models, schemas, enums

'''
    Create Objects
'''
def add_exercise(db: Session, exercise: schemas.ExerciseCreate):
    
    db_exercise = models.Exercise(name=exercise.name, instructions=exercise.instructions, video=exercise.video)
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
                            exercise_id=media.exercise_id)
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return db_media

def add_alternative(db: Session, alternative: schemas.Alternative):
    exercise_info = db.query(models.Exercise).get(alternative.exercise_id)
    alternative_info = db.query(models.Exercise).filter(models.Exercise.name == alternative.alternative_name).first()
    exercise_info.alternative.append(alternative_info)
    db.commit()
    db.refresh()
    return alternative_info
    
'''
    Read Objects
'''


def get_exercises(db: Session, skip: int = 0, limit: int = 100):
    exercise_set = db.query(models.Exercise).offset(skip).limit(limit).all()
    response = []
    for exercise in exercise_set:
        item = {
            "id": exercise.id,   
            "name": exercise.name,
            "instructions": exercise.instructions,
            "video": exercise.video,
            "details": exercise.details,
            "media": exercise.media,
            "alternatives": []
        }
        for alternative in exercise.alternative:
            item["alternatives"].append(alternative.id)
        response.append(item)
    
    return response

def get_exercises_by_type(db: Session, exercise_type: enums.TypeEnum , skip: int = 0, limit: int = 100):
    type_set = db.query(models.Exercise).\
                    join(models.Detail, models.Exercise.id == models.Detail.exercise_id).\
                    filter(models.Detail.type == exercise_type).\
                    all()
    response = []
    for exercise in type_set:
        item = {
            "id": exercise.id,   
            "name": exercise.name,
            "instructions": exercise.instructions,
            "video": exercise.video,
            "details": exercise.details,
            "media": exercise.media,
            "alternatives": []
        }
        for alternative in exercise.alternative:
            item["alternatives"].append(alternative.id)
        response.append(item)
    
    return response

def get_exercises_by_muscle(db: Session, exercise_muscle: enums.MuscleEnum, skip: int = 0, limit: int = 100):
    muscle_set = db.query(models.Exercise).\
                join(models.Detail, models.Exercise.id == models.Detail.exercise_id).\
                filter(models.Detail.main_muscle == exercise_muscle).\
                all()
    response = []
    for exercise in muscle_set:
        item = {
            "id": exercise.id,   
            "name": exercise.name,
            "instructions": exercise.instructions,
            "video": exercise.video,
            "details": exercise.details,
            "media": exercise.media,
            "alternatives": []
        }
        for alternative in exercise.alternative:
            item["alternatives"].append(alternative.id)
        response.append(item)
    
    return response

def get_exercises_by_equipment(db: Session, exercise_equipment: enums.EquipmentEnum, skip: int = 0, limit: int = 100):
    equipment_set = db.query(models.Exercise).\
                join(models.Detail, models.Exercise.id == models.Detail.exercise_id).\
                filter(models.Detail.equipment == exercise_equipment).\
                all()
    response = []
    for exercise in equipment_set:
        item = {
            "id": exercise.id,   
            "name": exercise.name,
            "instructions": exercise.instructions,
            "video": exercise.video,
            "details": exercise.details,
            "media": exercise.media,
            "alternatives": []
        }
        for alternative in exercise.alternative:
            item["alternatives"].append(alternative.id)
        response.append(item)
    
    return response

def get_exercise(db: Session, exercise_id: int):
    exercise_item = db.query(models.Exercise).filter(models.Exercise.id == exercise_id).first()
    if exercise_item == None:
        return None

    response = {
            "id": exercise_item.id,   
            "name": exercise_item.name,
            "instructions": exercise_item.instructions,
            "video": exercise_item.video,
            "details": exercise_item.details,
            "media": exercise_item.media,
            "alternatives": []
        }
    for alternative in exercise_item.alternative:
        response["alternatives"].append(alternative.id)
    
    return response

def get_exercise_id(db: Session, exercise_name: str):
    response = db.query(models.Exercise).filter(models.Exercise.name == exercise_name).first()
    return response.id