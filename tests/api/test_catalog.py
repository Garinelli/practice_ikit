import requests

from schemes import (Catalog, Offer, RootMini, 
                      ProductByCode, Product, ProductFilter)

def test_get_catalog(base_url):
    request = requests.get(f'{base_url}/catalog')
    data = request.json()
    assert request.status_code == 200
    assert len(data)

def test_get_existent_catalog(base_url):
    request = requests.get(f'{base_url}/catalog/avtotovary')
    data = request.json()
    assert request.status_code == 200
    assert len(data)
    Catalog(**data['children'][0])
    assert True

def test_get_non_existent_catalog(base_url):
    request = requests.get(f'{base_url}/catalog/qwerty')
    assert request.status_code == 404
    assert request.json() == {'message': 'Not found'}

def test_get_offers(base_url):
    request = requests.get(f'{base_url}/catalog/offers')
    data = request.json()
    assert request.status_code == 200
    assert data
    Offer(**data[0])
    assert True 

def test_get_offer_tabs(base_url):
    request = requests.get(f'{base_url}/catalog/offers/tabs')
    data = request.json()
    assert request.status_code == 200
    assert data 
    Offer(**data[0])
    assert True 

def test_get_root_mini(base_url):
    request = requests.get(f'{base_url}/catalog/root-mini')
    data = request.json()
    assert request.status_code == 200
    assert data
    RootMini(**data[0])
    assert True 

def test_get_last_seen(base_url):
    request = requests.get(f'{base_url}/catalog/last-seen')
    data = request.json()
    assert request.status_code == 200
    assert not data

def test_get_products_by_code(base_url):
    request = requests.get(f'{base_url}/catalog/products-by-code')
    data = request.json()
    assert request.status_code == 200
    assert data['data']
    ProductByCode(**data['data'][0])
    assert True

def test_get_slug_products(base_url):
    request = requests.get(f'{base_url}/catalog/avtotovary/products')
    data = request.json()
    assert request.status_code == 200
    assert len(data['data'])
    Product(**data['data'][0])
    assert True 

def test_get_slug_products_filter(base_url):
    request = requests.get(f'{base_url}/catalog/avtotovary/filter')
    data = request.json()
    assert request.status_code == 200
    assert 'filter' in data
    assert data['filter']
    ProductFilter(**data['filter'][0])
    assert True 
