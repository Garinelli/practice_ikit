import requests

from schemes import Session

def test_get_session(base_url):
    request = requests.get(f'{base_url}/session')
    data = request.json()
    assert request.status_code == 200
    Session(**data)
    assert True
    