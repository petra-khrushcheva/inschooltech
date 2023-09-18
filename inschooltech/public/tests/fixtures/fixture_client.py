import pytest
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_token(api_client, user):
    response = api_client.post(
        '/auth/jwt/create/',
        dict(username=user.username, password='somep4$$')
    )
    token = response.data["access"]
    bearer = f'Bearer {token}'
    return bearer
