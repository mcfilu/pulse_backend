from fastapi import APIRouter
import requests

router = APIRouter()


@router.get("/users/{user_id}", tags=["users"])
async def get_user(user_id: int):
    response = requests.get(f"https://reqres.in/api/users/{user_id}")
    return response.json()
    # return {"Message": "hello"}