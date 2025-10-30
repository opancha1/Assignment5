from fastapi import FastAPI
from api.models import models
from api.dependencies.database import engine
from api.controllers import sandwiches

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(sandwiches.router)

@app.get("/")
def home():
    return {"message": "Sandwich Maker API running ✅"}