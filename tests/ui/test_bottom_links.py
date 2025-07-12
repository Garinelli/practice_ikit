import time 
 
from selenium.webdriver.common.by import By

def scroll_page_to_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # подождать загрузки контента
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break  # достигли конца страницы
        last_height = new_height

def test_open_catalog_page(driver, host_name):
    driver.get(host_name)
    time.sleep(1)
    scroll_page_to_bottom(driver)
    driver.find_element(By.CSS_SELECTOR, 'a[href*="/catalog"]').click()
    time.sleep(1)
    assert driver.current_url == f'{host_name}/catalog'

def test_open_sale_page(driver, host_name):
    driver.get(host_name)
    time.sleep(1)
    scroll_page_to_bottom(driver)
    driver.find_element(By.CSS_SELECTOR, 'a[href*="/sale"]').click()
    time.sleep(1)
    assert driver.current_url == f'{host_name}/sale'

def test_open_brands_page(driver, host_name):
    driver.get(host_name)
    time.sleep(1)
    scroll_page_to_bottom(driver)
    driver.find_element(By.CSS_SELECTOR, 'a[href*="/brands"]').click()
    time.sleep(1)
    assert driver.current_url == f'{host_name}/brands'

def test_open_services_page(driver, host_name):
    driver.get(host_name)
    time.sleep(1)
    scroll_page_to_bottom(driver)
    driver.find_element(By.CSS_SELECTOR, 'a[href*="/services"]').click()
    time.sleep(1)
    assert driver.current_url == f'{host_name}/services'

def test_open_blog_page(driver, host_name):
    driver.get(host_name)
    time.sleep(1)
    scroll_page_to_bottom(driver)
    driver.find_element(By.CSS_SELECTOR, 'a[href*="/blog"]').click()
    time.sleep(1)
    assert driver.current_url == f'{host_name}/blog'
