import time

from selenium.webdriver.common.by import By

def test_registration(driver, host_name):
    driver.get(f'{host_name}/registration')
    time.sleep(2)
    driver.find_element(By.ID, 'v-0-0-0-0').send_keys('Имя')
    driver.find_element(By.ID, 'v-0-0-0-1').send_keys('Фамилия')
    driver.find_element(By.ID, 'v-0-0-0-4').send_keys('9000000000')
    driver.find_element(By.ID, 'v-0-0-0-5').send_keys('useremail@mail.ru')
    driver.find_element(By.ID, 'v-0-0-0-6').send_keys('userpassword123Q')
    driver.find_element(By.ID, 'v-0-0-0-7').send_keys('userpassword123Q')
    
    buttons = driver.find_elements(By.TAG_NAME, 'button')
    agree_button = buttons[-2]
    register_button = buttons[-1]
    agree_button.click()
    register_button.click()
    time.sleep(3)
    assert driver.find_element(By.CLASS_NAME, 'font-semibold.text-lg').text == '+7 (900) 000-00-00.'
