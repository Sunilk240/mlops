import pytest
from app.api.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {'status': 'healthy'}

def test_predict_positive(client):
    response = client.post('/predict', json={'text': 'This is a great product!'})
    assert response.status_code == 200
    data = response.json
    assert 'prediction' in data
    assert 'sentiment' in data
    assert 'confidence' in data
    assert data['sentiment'] == 'positive'
    assert data['prediction'] == 1
    assert 0 <= data['confidence'] <= 1

def test_predict_negative(client):
    response = client.post('/predict', json={'text': 'This is a terrible product!'})
    assert response.status_code == 200
    data = response.json
    assert data['sentiment'] == 'negative'
    assert data['prediction'] == 0
    assert 0 <= data['confidence'] <= 1

def test_predict_empty_text(client):
    response = client.post('/predict', json={'text': ''})
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'No text provided'

def test_predict_missing_text(client):
    response = client.post('/predict', json={})
    assert response.status_code == 400
    assert 'error' in response.json
    assert response.json['error'] == 'No text provided'

def test_predict_invalid_json(client):
    response = client.post('/predict', data='invalid json')
    assert response.status_code == 400
    assert 'error' in response.json

def test_predict_long_text(client):
    long_text = "This is a great product! " * 100  # Create a long text
    response = client.post('/predict', json={'text': long_text})
    assert response.status_code == 200
    data = response.json
    assert 'prediction' in data
    assert 'sentiment' in data
    assert 'confidence' in data

def test_predict_special_characters(client):
    response = client.post('/predict', json={'text': '!@#$%^&*()_+ This is great! 😊'})
    assert response.status_code == 200
    data = response.json
    assert 'prediction' in data
    assert 'sentiment' in data
    assert 'confidence' in data

def test_predict_numbers(client):
    response = client.post('/predict', json={'text': '12345 This is great!'})
    assert response.status_code == 200
    data = response.json
    assert 'prediction' in data
    assert 'sentiment' in data
    assert 'confidence' in data

def test_predict_mixed_case(client):
    response = client.post('/predict', json={'text': 'ThIs Is A gReAt PrOdUcT!'})
    assert response.status_code == 200
    data = response.json
    assert 'prediction' in data
    assert 'sentiment' in data
    assert 'confidence' in data 