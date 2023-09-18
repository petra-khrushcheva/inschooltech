import pytest


@pytest.mark.django_db
def test_lab_results_anauthorized(api_client):
    response = api_client.get('/api/public/tests/')
    assert response.status_code == 401


@pytest.mark.django_db
def test_lab_results(auth_api_client, assessment, lab, score, indicator):
    response = auth_api_client.get('/api/public/tests/')
    assert response.status_code == 200
    assert response.json()[0]['id'] == assessment.id
    assert response.json()[0]['duration_seconds'] == 5
    assert response.json()[0]['lab_id'] == lab.id
    assert response.json()[0]['results'][0]['id'] == score.id
    assert response.json()[0]['results'][0]['indicator_name'] == indicator.name
