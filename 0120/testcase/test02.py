from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
class post_content(unittest.TestCase):
   
    def test_01_login(self):
        # driver = self.driver
        driver.get('https://baidu.com')


if __name__ == "__main__":
    unittest.main(verbosity =2)



