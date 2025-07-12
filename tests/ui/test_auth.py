import time 

from selenium.webdriver.common.by import By 

def test_auth(driver, host_name):
    driver.get(f'{host_name}/auth')
    time.sleep(2)
    phone_number_button = driver.find_element(By.ID, 'v-0-0-0-0-trigger-M_0wyA8IxIbOl2UvzXk0xFwWMN9IuOYzf_-kww-OiUY')
    phone_number_button.click()
    driver.find_element(By.ID, 'v-0-0-0-3').send_keys('9082009829')
    driver.find_elements(By.TAG_NAME, 'button')[-1].click()
    time.sleep(2)
    assert driver.find_element(By.CLASS_NAME, 'font-semibold.text-lg').text.strip() == '+7 (908) 200-98-29'
