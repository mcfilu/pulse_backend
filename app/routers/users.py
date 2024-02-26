from fastapi import APIRouter
from pydantic import BaseModel
import requests

router = APIRouter()

#blueprint for pydantic basemodel class that represents the outputed data
class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

#
@router.get("/users/{user_id}", tags=["users"])
async def get_user(user_id: int) -> UserData:
    response = requests.get(f"https://reqres.in/api/users/{user_id}")
    user_instance = UserData(**response.json()['data'])
    return user_instance
    # return {"Message": "hello"}