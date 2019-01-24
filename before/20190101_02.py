import selenium
from selenium import webdriver 
import unittest
import time
from selenium.webdriver.common.action_chains  import ActionChains

driver = webdriver.Chrome()
driver.get("https://baidu.com")
elem = driver.find_element_by_css_selector('a[name = "tj_briicon"]')
ActionChains(driver).move_to_element(elem).perform()
elem_music = driver.find_element_by_css_selector('a[name = "tj_mp3"]')
ActionChains(driver).move_to_element(elem_music).click().perform()
driver.save_screenshot("./001.png")
time.sleep(3)
driver.quit()