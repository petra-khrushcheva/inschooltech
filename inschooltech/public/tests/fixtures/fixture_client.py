import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def auth_api_client(db, user):
    auth_client = APIClient()
    response = auth_client.post(
        '/auth/jwt/create/',
        dict(username=user.username, password='somep4$$')
    )
    token = response.data["access"]
    bearer = f'Bearer {token}'
    auth_client.credentials(HTTP_AUTHORIZATION=bearer)
    yield auth_client
    auth_client.credentials(HTTP_AUTHORIZATION="")
