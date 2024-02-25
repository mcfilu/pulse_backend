from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Message": "Welcome to the application, please refer to the /docs to check the api functionality"}