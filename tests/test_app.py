from app import app
import pytest

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, I am Catherine and this is my Containerized Flask App Successfully deployed on Heroku' in response.data
