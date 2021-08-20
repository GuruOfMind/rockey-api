# rempve any relative imports
import schemas
import json
import crud

import models
from database import SessionLocal, engine

db = SessionLocal()

models.Base.metadata.create_all(bind=engine)

with open("data/resources/exercises_database.json", "r") as data_source:
    data = json.load(data_source)

    for item in data:

        '''
            add exercise
        '''
        # db_record = models.Exercise(name=item["name"], instructions=item["instructions"], video=item["video"])
        # db.add(db_record)
        
        '''
            add alternatives
        '''
        # exercise_id = crud.get_exercise_id(db=db, exercise_name=item["name"])
        # for alternative in item["alternative"]:
        #     crud.add_alternative(db=db, alternative=schemas.Alternative(exercise_id=exercise_id, alternative_name=alternative))

        '''
            add details and media
        '''
        # exercise_id = crud.get_exercise_id(db=db, exercise_name=item["name"])
        # crud.add_details(db= db, details=models.Detail(type=item["details"]["type"], main_muscle=item["details"]["main_muscle"], equipment=item["details"]["equipment"], exercise_id=exercise_id))
        # crud.add_media(db=db, media=models.Media(figure_img=item["images"]["image_1"], figure_url=item["images"]["image_1_url"], exercise_id=exercise_id))
        # crud.add_media(db=db, media=models.Media(figure_img=item["images"]["image_2"], figure_url=item["images"]["image_2_url"], exercise_id=exercise_id))

    db.commit()

db.close()