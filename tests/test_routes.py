import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app('testing')
    with app.test_client() as client:
        with app.app_context():
            yield client

def test_home_route_returns_hello_world(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, world!"}

def test_home_route_returns_404_for_non_existing_routes(client):
    response = client.get('/non-existing')
    assert response.status_code == 404