import time 

from selenium.webdriver.common.by import By

def test_get_stores(driver, host_name):
    driver.get(host_name)
    driver.find_element(By.XPATH, "//span[text()='Магазины']").click()
    time.sleep(1)
    assert driver.current_url == f'{host_name}/company/stores'

def test_get_moscow_city(driver, host_name):
    driver.get(host_name)
    time.sleep(3)
    driver.find_element(By.XPATH, "//span[text()='Красноярск']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[text()='Москва']").click()
    time.sleep(3)
    assert driver.current_url == 'https://msk.virage24.ru/'

def test_get_krasnodar_city(driver, host_name):
    driver.get(host_name)
    time.sleep(3)
    driver.find_element(By.XPATH, "//span[text()='Красноярск']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[text()='Краснодар']").click()
    time.sleep(3)
    assert driver.current_url == 'https://krd.virage24.ru/'

def test_get_another_city(driver, host_name):
    """Тест на переключение города, в котором нет магазина (физически)""" 
    driver.get(host_name)
    time.sleep(3)
    driver.find_element(By.XPATH, "//span[text()='Красноярск']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[text()='Воронеж']").click()
    time.sleep(3)
    assert driver.current_url == 'https://www.virage24.ru/'
