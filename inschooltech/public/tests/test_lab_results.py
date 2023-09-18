import pytest


@pytest.mark.django_db
def test_lab_results(api_client, user_token):
    api_client.credentials(HTTP_AUTHORIZATION=user_token)
    response = api_client.get('/api/public/tests/')
    assert response.status_code == 200
