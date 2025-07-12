import time 
 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def test_open_catalog(driver, host_name):
    driver.get(host_name)
    time.sleep(3)
    # Закрываем окно 'Ваше текущее местоположение'
    city_button = driver.find_elements(By.XPATH, "//button[contains(@aria-disabled,'false')]")
    if city_button:
        city_button[0].click()
    driver.find_element(By.CSS_SELECTOR, 'a[href*="/catalog"]').click()
    time.sleep(1)
    assert driver.current_url == f'{host_name}/catalog'

def test_open_gruzopodieemnoe_oborudovanie_takelaz(driver, host_name):
    driver.get(host_name)
    time.sleep(3)
    # Закрываем окно 'Ваше текущее местоположение'
    city_button = driver.find_elements(By.XPATH, "//button[contains(@aria-disabled,'false')]")
    if city_button:
        city_button[0].click()
    driver.find_element(By.CSS_SELECTOR, 'a[href*="/catalog"]').click()
    actions = ActionChains(driver)
    # Перемещаем курсор
    actions.move_by_offset(100, 150).perform()
    time.sleep(1)
    categories_element_div = driver.find_element(By.CSS_SELECTOR, 'div.categories-grid')
    avtotovary = categories_element_div.find_elements(By.TAG_NAME, 'a')[4]
    avtotovary.click()
    time.sleep(1)
    assert driver.current_url == f'{host_name}/catalog/gruzopodieemnoe-oborudovanie-takelaz'

def test_open_avtotovary(driver, host_name):
    driver.get(host_name)
    time.sleep(3)
    # Закрываем окно 'Ваше текущее местоположение'
    city_button = driver.find_elements(By.XPATH, "//button[contains(@aria-disabled,'false')]")
    if city_button:
        city_button[0].click()
    driver.find_element(By.CSS_SELECTOR, 'a[href*="/catalog"]').click()
    actions = ActionChains(driver)
    # Перемещаем курсор
    actions.move_by_offset(100, 200).perform()
    time.sleep(1)
    categories_element_div = driver.find_element(By.CSS_SELECTOR, 'div.categories-grid')
    avtotovary = categories_element_div.find_elements(By.TAG_NAME, 'a')[0]
    avtotovary.click()
    time.sleep(1)
    assert driver.current_url == f'{host_name}/catalog/avtotovary'

def test_open_instrumenty_i_osnastka(driver, host_name):
    driver.get(host_name)
    time.sleep(3)
    # Закрываем окно 'Ваше текущее местоположение'
    city_button = driver.find_elements(By.XPATH, "//button[contains(@aria-disabled,'false')]")
    if city_button:
        city_button[0].click()
    driver.find_element(By.CSS_SELECTOR, 'a[href*="/catalog"]').click()
    actions = ActionChains(driver)
    # Перемещаем курсор
    actions.move_by_offset(100, 200).perform()
    time.sleep(1)
    categories_element_div = driver.find_element(By.CSS_SELECTOR, 'div.categories-grid')
    avtotovary = categories_element_div.find_elements(By.TAG_NAME, 'a')[1]
    avtotovary.click()
    time.sleep(1)
    assert driver.current_url == f'{host_name}/catalog/instrumenty-i-osnastka'

def test_open_oborudovanie_i_texnika(driver, host_name):
    driver.get(host_name)
    time.sleep(3)
    # Закрываем окно 'Ваше текущее местоположение'
    city_button = driver.find_elements(By.XPATH, "//button[contains(@aria-disabled,'false')]")
    if city_button:
        city_button[0].click()
    driver.find_element(By.CSS_SELECTOR, 'a[href*="/catalog"]').click()
    actions = ActionChains(driver)
    # Перемещаем курсор
    actions.move_by_offset(100, 200).perform()
    time.sleep(1)
    categories_element_div = driver.find_element(By.CSS_SELECTOR, 'div.categories-grid')
    avtotovary = categories_element_div.find_elements(By.TAG_NAME, 'a')[2]
    avtotovary.click()
    time.sleep(1)
    assert driver.current_url == f'{host_name}/catalog/oborudovanie-i-texnika'

def test_open_pnevmatika_gidravlika(driver, host_name):
    driver.get(host_name)
    time.sleep(3)
    # Закрываем окно 'Ваше текущее местоположение'
    city_button = driver.find_elements(By.XPATH, "//button[contains(@aria-disabled,'false')]")
    if city_button:
        city_button[0].click()
    driver.find_element(By.CSS_SELECTOR, 'a[href*="/catalog"]').click()
    actions = ActionChains(driver)
    # Перемещаем курсор
    actions.move_by_offset(100, 200).perform()
    time.sleep(1)
    categories_element_div = driver.find_element(By.CSS_SELECTOR, 'div.categories-grid')
    avtotovary = categories_element_div.find_elements(By.TAG_NAME, 'a')[3]
    avtotovary.click()
    time.sleep(1)
    assert driver.current_url == f'{host_name}/catalog/pnevmatika-gidravlika'
