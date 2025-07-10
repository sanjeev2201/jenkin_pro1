from app import app
# import pytest
# from fastapi.testclient import TestClient
def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Hello from Flask + Jenkins!' in response.data