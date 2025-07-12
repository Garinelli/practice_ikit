import time 

from selenium.webdriver.common.by import By

def test_open_orders_page(driver, host_name):
    driver.get(host_name)
    driver.find_element(By.XPATH,  "//a[contains(@title,'Заказы')]").click()
    time.sleep(3)
    no_products_text = driver.find_elements(By.CSS_SELECTOR, ".text-center.text-xl.desktop\\:text-2xl") 
    assert no_products_text
    assert no_products_text[0].text == 'Нет заказов'
