from fastapi import FastAPI
from .routers import users

app = FastAPI()

app.include_router(users.router)

@app.get("/")
async def root():
    return {"message": "me owow"}

@app.get("/me")
async def new():
    return {"user": "me"}