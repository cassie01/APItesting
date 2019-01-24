from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
mobileEmulatio = {"deviceName":'iPad'}
chrome_options.add_experimental_option('mobileEmulation',mobileEmulatio)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.baidu.com')