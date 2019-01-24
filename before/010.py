from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains

class Cnode(unittest.TestCase):
    def setUp(self):
        self.Url = 'http://39.107.96.138:3000'
        self.driver = webdriver.Chrome()
        self.driver.get(self.Url)
        #登陆用户
        self.driver.find_element_by_css_selector('a[href = "/signin"]').click()
        self.driver.find_element_by_id('name').send_keys('user1')
        self.driver.find_element_by_id('pass').send_keys('123456')
        self.driver.find_element_by_css_selector('input[type = "submit"]').click()
    
    def test_post_topic(self):
        driver = self.driver
        driver.get('http://39.107.96.138:3000/topic/create')
        driver.find_element_by_name('tab').click()
        driver.find_element_by_css_selector('[value="share"]').click()
        driver.find_element_by_id('title').send_keys('金丝熊000001新熊发帖')
        content_area = driver.find_element_by_class_name('CodeMirror-scroll')
        content_area.click()
        ActionChains(driver).move_to_element(content_area).send_keys('可乐饲养员测试').perform()
        driver.find_element_by_css_selector('input[type="submit"]').click()


    def tearDown(self):
        self.driver.save_screenshot('./01.png')
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main()