import requests

def test_main_page(base_url):
    request = requests.get(base_url)
    assert request.status_code == 404
    assert request.json() == {'message': 'Not found'}
