from fastapi import FastAPI
from .routers import users
from fastapi.middleware.cors import CORSMiddleware



app = FastAPI()

app.include_router(users.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

"""
The basic / endpoint that suits for the devs who mistakenly input it, showcases where to obtain the docs and more detailed info
"""
@app.get("/")
async def root():
    return {"message": "Welcome to the application, please refer to the /docs url to check the api functionality"}
