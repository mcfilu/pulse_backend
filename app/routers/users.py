from fastapi import APIRouter, HTTPException
from ..helpers.users import transform_user, UserData
import httpx

router = APIRouter()



@router.get("/users/{user_id}", tags=["users"])
async def get_user(user_id: int) -> UserData:
    """
    Api endpoint at /users/id that loads the user info from the int argument passed to the url and utilises HTTP request to the regres.in external api, 
    takes the information from ['data'], ommits the unecessary data, puts that into the pydantic object
    and returns it to the client.\n\n
    Raises:
        HTTPException: If regres.in api returns any other code than 200, the HTTPException is raised, the corresponding HTTP status code passed and the error message displayed.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://reqres.in/api/users/{user_id}")
    if response.status_code != 200:
        raise HTTPException(status_code = response.status_code, detail=f"Error accessing regres.in Api at /users/{user_id} ")

    user_instance = transform_user(response)
    return user_instance
