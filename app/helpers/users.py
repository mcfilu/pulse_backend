from pydantic import BaseModel

#blueprint for pydantic basemodel class that represents the outputed data
class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

def transform_user(resp):
    return UserData(**resp.json().['data'])