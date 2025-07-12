import requests

from schemes import City

def test_cities(base_url):
    request = requests.get(f'{base_url}/cities')
    data = request.json()
    assert request.status_code == 200
    assert data['data']

def test_get_cities_suggest(base_url):
    request = requests.get(f'{base_url}/cities/suggest')
    data = request.json()
    assert request.status_code == 200
    City(**data[0])
    assert True

