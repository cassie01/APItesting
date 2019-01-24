from selenium import webdriver
import unittest
import time

"""
user: testuser01
password: 123456
"""
class Cnode(unittest.TestCase):

    def setUp(self):
        self.Url = 'http://39.107.96.138:3000'
        self.driver = webdriver.Chrome()
        self.driver.get(self.Url)
    
    def test_a_register(self):
        driver = self.driver
        driver.find_element_by_css_selector('a[href = "/signup"]').click()
        driver.find_element_by_id('loginname').send_keys('lch940517')
        driver.find_element_by_id('pass').send_keys('666')
        driver.find_element_by_id('re_pass').send_keys('666')
        driver.find_element_by_id('email').send_keys('377041471@qq.com')
        driver.find_element_by_css_selector('input[type = "submit"]').click()
        time.sleep(4)

    def test_b_login(self):
        driver = self.driver
        driver.find_element_by_css_selector('a[href = "/signin"]').click()
        driver.find_element_by_id('name').send_keys('lch940517')
        driver.find_element_by_id('pass').send_keys('666')
        driver.find_element_by_css_selector('input[type = "submit"]').click()

    
    def tearDown(self):
        self.driver.save_screenshot('./a1.png')
        self.driver.quit()

if __name__== "__main__":
    unittest.main()