from fastapi import FastAPI
from app.config import env
from app.routers import whatsapp
from dotenv import load_dotenv

load_dotenv(override=True)

app = FastAPI()

app.include_router(whatsapp.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}
