from django.test import TestCase
import requests

def test_create_person():
    response = requests.post('http://localhost:8000/api/', json={'name': 'Mark Essien'})
    assert response.status_code == 201
    assert response.json()['name'] == 'Mark Essien'
  

def test_retrieve_person():
    response = requests.get('http://localhost:8000/api/1/')
    assert response.status_code == 200
    assert response.json()['name'] == 'Mark Essien'
  

def test_update_person():
    response = requests.put('http://localhost:8000/api/1/', json={'name': 'Mark Hngx'})
    assert response.status_code == 200
    assert response.json()['name'] == 'Mark Hngx'
    
def test_delete_person():
    response = requests.delete('http://localhost:8000/api/1/')
    assert response.status_code == 204

if __name__ == '__main__':
    test_create_person()
    test_retrieve_person()
    test_update_person()
    test_delete_person()
