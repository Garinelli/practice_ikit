import time 

from selenium.webdriver.common.by import By 

def test_search(driver, host_name):
    product_name = 'hyundai'
    driver.get(host_name)
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[contains(@placeholder,'Найти...')]").send_keys(product_name)
    driver.find_element(By.CLASS_NAME, 'h-full.w-11.-outline-offset-4').click()
    time.sleep(3)
    search_result_text = driver.find_elements(By.TAG_NAME, 'h1')
    assert search_result_text[0].text == f'Результаты поиска: {product_name}'
    assert driver.current_url == f'{host_name}/search?term={product_name}'
