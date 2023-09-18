import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture
def user():
    user_1 = User.objects.create_user(
        email='testuser@example.com',
        username='testuser',
        password='somep4$$'
    )
    return user_1
