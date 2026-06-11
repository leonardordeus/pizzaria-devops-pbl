import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_status_endpoint(client):
    """Testa se o endpoint de status responde com sucesso (200)"""
    response = client.get('/status')
    assert response.status_code == 200
