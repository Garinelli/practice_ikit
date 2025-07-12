import time 

from selenium.webdriver.common.by import By

def test_get_contacts_page(driver, host_name):
    driver.get(host_name)
    time.sleep(3)
    driver.find_element(By.XPATH,  "//a[contains(@title,'Контакты')]").click()
    time.sleep(1)
    assert driver.current_url == f'{host_name}/company/contacts'
