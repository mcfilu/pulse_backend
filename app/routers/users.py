from fastapi import APIRouter
import requests

router = APIRouter()


@router.get("/users/{user_id}", tags=["users"])
async def get_user(user_id: int):
    return {"username": user_id}