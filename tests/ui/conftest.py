import pytest 
from selenium import webdriver

chrome_driver = webdriver.Chrome()
chrome_driver.get('https://www.virage24.ru')
chrome_driver.set_window_size(1920, 1080)

@pytest.fixture(scope='module')
def driver():
    return chrome_driver

@pytest.fixture(scope='module')
def host_name():
    return 'https://www.virage24.ru'
