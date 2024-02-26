from app.helpers.users import transform_user
import requests

def test_transform_user():
    response = requests.get('https://reqres.in/api/users/2')
    user_instance = transform_user(response)
    assert user_instance.id == 2
    assert user_instance.email == 'janet.weaver@reqres.in'
    assert user_instance.first_name == 'Janet'
    assert user_instance.last_name == 'Weaver'
    assert user_instance.avatar == 'https://reqres.in/img/faces/2-image.jpg'