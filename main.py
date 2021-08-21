from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from src import config
from src.routes import exercises as exercises_router
from src.database.database import engine
import src.models as models 


# models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=f"API for {config.SERVICE_NAME}",
    description="visit <URL>/docs for documentation"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(exercises_router.router)

@app.get("/")
async def home():
    response = {
        "error":{
            "message": f"This API is for Exercises data, {config.SERVICE_NAME}."
        }
    }
    print("____________________________________________")
    print(config.BASE_DIR)
    print("____________________________________________")
    return JSONResponse(content=response)
