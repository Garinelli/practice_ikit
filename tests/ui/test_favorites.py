import time 

from selenium.webdriver.common.by import By

def test_add_product_to_favorites(driver, host_name):
    driver.get(host_name)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.break-words.max-tablet\\:group-vanilla-hover\\:invisible.line-clamp-3').click()
    product_code = driver.find_element(By.CLASS_NAME, 'shrink-0').text  
    time.sleep(2)
    buttons = driver.find_element(By.CSS_SELECTOR, ".flex.gap-1\\.5")
    buttons.find_element(By.TAG_NAME, 'button').click()
    time.sleep(2)
    driver.find_element(By.XPATH,  "//a[contains(@title,'Избранное')]").click()
    cart_product_code = driver.find_elements(By.CLASS_NAME, 'shrink-0')[3].text
    assert product_code == cart_product_code
