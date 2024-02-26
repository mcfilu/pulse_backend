from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from helpers.users import transform_user
import requests

router = APIRouter()


"""
api endpoiint at /users/<int> that loads the user info from regres.in external api, 
takes the information from ['data'], ommits the unecessary data, puts that into the pydantic object
and return to client
"""
@router.get("/users/{user_id}", tags=["users"])
async def get_user(user_id: int) -> UserData:
    response = requests.get(f"https://reqres.in/api/users/{user_id}")
    if response.status_code != 200:
        raise HTTPException(status_code = response_status_code, detail=f"Error accessing regres.in Api at /users/{user_id} ")

    user_instance = transform_user(response)
    return user_instance
