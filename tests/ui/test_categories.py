import time 

from selenium.webdriver.common.by import By

def test_open_auto_products_category(driver, host_name):
    driver.get(host_name)
    time.sleep(2)
    # Закрываем окно 'Ваше текущее местоположение'
    city_button = driver.find_elements(By.XPATH, "//button[contains(@aria-disabled,'false')]")
    if city_button:
        city_button[0].click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[text()='Автотовары']").click()
    time.sleep(2)
    assert driver.current_url == f'{host_name}/catalog/avtotovary'

def test_open_tools_category(driver, host_name):
    driver.get(host_name)
    time.sleep(2)
    # Закрываем окно 'Ваше текущее местоположение'
    city_button = driver.find_elements(By.XPATH, "//button[contains(@aria-disabled,'false')]")
    if city_button:
        city_button[0].click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[text()='Инструменты и оснастка']").click()
    time.sleep(2)
    assert driver.current_url == f'{host_name}/catalog/instrumenty-i-osnastka'

def test_open_equipment_category(driver, host_name):
    driver.get(host_name)
    time.sleep(2)
    # Закрываем окно 'Ваше текущее местоположение'
    city_button = driver.find_elements(By.XPATH, "//button[contains(@aria-disabled,'false')]")
    if city_button:
        city_button[0].click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(@title,'Оборудование и техника')]").click()
    time.sleep(2)
    assert driver.current_url == f'{host_name}/catalog/oborudovanie-i-texnika'

def test_open_hydraulics_category(driver, host_name):
    driver.get(host_name)
    time.sleep(2)
    # Закрываем окно 'Ваше текущее местоположение'
    city_button = driver.find_elements(By.XPATH, "//button[contains(@aria-disabled,'false')]")
    if city_button:
        city_button[0].click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(@title,'Пневматика, гидравлика')]").click()
    time.sleep(2)
    assert driver.current_url == f'{host_name}/catalog/pnevmatika-gidravlika'

def test_open_gruzopodieemnoe_category(driver, host_name):
    driver.get(host_name)
    time.sleep(2)
    # Закрываем окно 'Ваше текущее местоположение'
    city_button = driver.find_elements(By.XPATH, "//button[contains(@aria-disabled,'false')]")
    if city_button:
        city_button[0].click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(@title,'Грузоподъемное оборудование, такелаж')]").click()
    time.sleep(2)
    assert driver.current_url == f'{host_name}/catalog/gruzopodieemnoe-oborudovanie-takelaz'

def test_open_ventilyatsiya_category(driver, host_name):
    driver.get(host_name)
    time.sleep(2)
    # Закрываем окно 'Ваше текущее местоположение'
    city_button = driver.find_elements(By.XPATH, "//button[contains(@aria-disabled,'false')]")
    if city_button:
        city_button[0].click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(@title,'Климат и вентиляция')]").click()
    time.sleep(2)
    assert driver.current_url == f'{host_name}/catalog/klimat-i-ventiliaciia'

"""------------------------------------------------------------------------------------------------------------"""
def test_open_sad_ogorod_category(driver, host_name):
    driver.get(host_name)
    time.sleep(2)
    # Закрываем окно 'Ваше текущее местоположение'
    city_button = driver.find_elements(By.XPATH, "//button[contains(@aria-disabled,'false')]")
    if city_button:
        city_button[0].click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(@title,'Сад, огород, отдых и туризм')]").click()
    time.sleep(2)
    assert driver.current_url == f'{host_name}/catalog/sad-ogorod-otdyx-i-turizm'

def test_open_electrical_goods_category(driver, host_name):
    driver.get(host_name)
    time.sleep(2)
    # Закрываем окно 'Ваше текущее местоположение'
    city_button = driver.find_elements(By.XPATH, "//button[contains(@aria-disabled,'false')]")
    if city_button:
        city_button[0].click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(@title,'Электротовары')]").click()
    time.sleep(2)
    assert driver.current_url == f'{host_name}/catalog/elektrotovary'
