def test_get_main_page(driver, host_name):
    driver.get(host_name)
    token = driver.get_cookie('sessionId')['value'] 
    assert token
    assert isinstance(token, str) 
    