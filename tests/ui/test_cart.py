import time 
 
from selenium.webdriver.common.by import By

def add_product_to_cart(driver, host_name):
    driver.get(f'{host_name}/product/kraska-akrilovaia-moiushhaiasia-13-kg-farbiteks-289838')
    time.sleep(3)
    add_to_cart_button = driver.find_elements(By.XPATH, "//button[contains(@aria-label,'В корзину')]")[-1]
    add_to_cart_button.click()

    product_code = driver.find_element(By.CLASS_NAME, 'shrink-0').text  
    print(f'{product_code = }')
    time.sleep(3)

    cart_icon = driver.find_element(By.XPATH, "//a[contains(@title,'Корзина')]")
    cart_icon.click()
    time.sleep(3)
    return product_code

def test_add_product_and_delete(driver, host_name):
    add_product_to_cart(driver, host_name)

    buttons = driver.find_element(By.CSS_SELECTOR, ".flex.gap-1\\.5")
    buttons.find_elements(By.TAG_NAME, 'button')[1].click()
    time.sleep(3)
    empty_cart_text = driver.find_elements(By.XPATH, "//p[text()='Ваша корзина пуста!']")
    assert empty_cart_text


def test_empty_cart(driver, host_name):
    driver.get(host_name)
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[contains(@title,'Корзина')]").click()
    time.sleep(3)
    empty_cart_text = driver.find_elements(By.XPATH, "//p[text()='Ваша корзина пуста!']")
    assert empty_cart_text

def test_add_product_to_cart(driver, host_name):
    product_code = add_product_to_cart(driver, host_name)

    cart_product_code = driver.find_elements(By.CLASS_NAME, 'shrink-0')[3].text 
    assert product_code == cart_product_code

def test_check_max_count(driver, host_name):
    add_product_to_cart(driver, host_name)
    quantity = driver.find_element(By.CSS_SELECTOR, ".leading-tight.underline.decoration-dotted.decoration-accent-safe").text
    quantity = int(quantity.split()[2]) 
    increment_button = driver.find_elements(By.CSS_SELECTOR, ".flex.items-center.justify-center.px-1")[-1]
    for _ in range(quantity*2):
        increment_button.click()
    current_count_str = driver.find_element(By.CSS_SELECTOR, ".hide-arrows.text-center.bg-opacity-50.outline-none.rounded.px-2").get_attribute("value")
    current_count = int(current_count_str)
    assert quantity == current_count

def test_check_correct_price(driver, host_name):
    add_product_to_cart(driver, host_name)
    
    current_price_span = driver.find_element(By.CSS_SELECTOR, ".text-nowrap.leading-tight.font-semibold.text-accent-secondary")
    current_price = int((current_price_span.find_element(By.TAG_NAME, 'span').text).replace(' ', ''))

    quantity = driver.find_element(By.CSS_SELECTOR, ".leading-tight.underline.decoration-dotted.decoration-accent-safe").text
    quantity = int(quantity.split()[2]) 
    increment_button = driver.find_elements(By.CSS_SELECTOR, ".flex.items-center.justify-center.px-1")[-1]
    for _ in range(quantity*2):
        increment_button.click()
    total_price_div =  driver.find_element(By.CSS_SELECTOR, ".flex.items-center.justify-between.text-xl.font-semibold")
    total_price_span = total_price_div.find_elements(By.TAG_NAME, 'span')[1]
    total_price = int((total_price_span.find_element(By.TAG_NAME, 'span').text).replace(' ', ''))
    assert current_price * quantity == total_price
