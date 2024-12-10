from fastapi import FastAPI
from app.routers import whatsapp

app = FastAPI()

app.include_router(whatsapp.router)


@app.get("/")
def read_root():
    return {"Hello": "World"}
