from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://baidu.com')

element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID,'kw'))
    )
element.send_keys('hahah')

