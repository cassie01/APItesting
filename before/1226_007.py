import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BaiDuSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_baidu_search(self):
        driver = self.driver
        driver.get('https://baidu.com')#获取并打开网页
        driver.find_element_by_id('kw').send_keys('仓鼠')
        driver.find_element_by_id('kw').send_keys(Keys.ENTER)
        time.sleep(4)

    def tear_down(self):
        self.driver.quit()
if __name__ == "__main__":
    unittest.main()
    


