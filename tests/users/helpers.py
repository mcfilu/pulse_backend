from app.helpers.users import transform_user

def test_transform_user():
    response = {
        'data': {
            'id': 1,
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'avatar': 'https://example.com/avatar.jpg'
        }
    }
    user_instance = transform_user(response)
    assert user_instance.id == 1
    assert user_instance.email == 'test@example.com'
    assert user_instance.first_name == 'John'
    assert user_instance.last_name == 'Doe'
    assert user_instance.avatar == 'https://example.com/avatar.jpg'