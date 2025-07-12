import requests

from schemes import SiteMapCatalogCategories, SiteMapLandings, SiteMapNews, SiteMapCatalogCategoriesTree

def test_get_sitemap_catalog_categories(base_url):
    request = requests.get(f'{base_url}/sitemap/catalogCategories')
    data = request.json()
    assert request.status_code == 200
    assert data
    SiteMapCatalogCategories(**data[0])
    assert True 

def test_get_sitemap_landings(base_url):
    request = requests.get(f'{base_url}/sitemap/landings')
    data = request.json()
    assert request.status_code == 200
    assert data 
    SiteMapLandings(**data[0])
    assert True 

def test_get_sitemap_news(base_url):
    request = requests.get(f'{base_url}/sitemap/news')
    data = request.json()
    assert request.status_code == 200
    assert data 
    SiteMapNews(**data[0])
    assert True 

def test_get_sitemap_catalog_categories_tree(base_url):
    request = requests.get(f'{base_url}/sitemap/catalogCategoriesTree')
    data = request.json()    
    assert request.status_code == 200 
    assert data 
    assert data[0]['children']
    SiteMapCatalogCategoriesTree(**data[0])
    assert True 

def test_get_sitemap_rent_categories_tree(base_url):
    request = requests.get(f'{base_url}/sitemap/rentCategoriesTree')
    data = request.json()    
    assert request.status_code == 200 
    assert data 
    assert not data[0]['children']
    SiteMapCatalogCategoriesTree(**data[0])
    assert True 

def test_get_sitemap_incorrect_param(base_url):
    request = requests.get(f'{base_url}/sitemap/rentsitemap123')
    data = request.json()
    assert request.status_code == 404
    assert data == {'message':'Not found'}
