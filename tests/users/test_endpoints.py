from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    user_data = response.json()
    assert user_data['id'] == 1
    assert user_data['email'] == 'george.bluth@reqres.in'