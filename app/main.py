from fastapi import FastAPI
from app.config import env
from app.routers import whatsapp

app = FastAPI()

app.include_router(whatsapp.router)

print(env.openai_api_key)

@app.get("/")
def read_root():
    return {"Hello": "World"}
