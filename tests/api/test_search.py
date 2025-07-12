import requests

def test_correct_search(base_url):
    product_name = 'hyundai'
    page = 1
    request = requests.get(f'{base_url}/catalog/search?page={page}&term={product_name}')
    data = request.json()
    assert request.status_code == 404
    assert data['query'] == product_name
    assert data['totalHits'] > 0
    assert data['products']
    assert not data['zeroQueries'] 
    assert data['page'] == page 
    assert data['last_page'] == page + 1

def test_non_existent_product_search(base_url):
    page = 1
    incorrect_product_name = 'qwertyQWE1555555'
    request = requests.get(f'{base_url}/catalog/search?page={page}&term={incorrect_product_name}')
    data = request.json()
    assert request.status_code == 404
    assert data['query'] == incorrect_product_name
    assert data['totalHits'] == 0
    assert not data['products']
    assert data['page'] == page
    assert data['last_page'] == page - 1

def test_search_preview(base_url):
    request = requests.get(f'{base_url}/catalog/search/preview')
    data = request.json()
    assert request.status_code == 200
    assert data
