import selenium
from selenium import webdriver 
import unittest
import time
from selenium.webdriver.common.action_chains  import ActionChains

class MorePruduction(unittest.TestCase):

    def setUp(self):
        print('start test')
        self.driver = webdriver.Chrome()
        
        
    def test_Cloud_music(self):
        driver = self.driver
        driver.get("https://baidu.com")
        elem = driver.find_element_by_css_selector('a[name = "tj_briicon"]')
        ActionChains(driver).move_to_element(elem).perform()

        elem_music = driver.find_element_by_css_selector('a[name = "tj_mp3"]')
        ActionChains(driver).move_to_element(elem_music).click().perform()


    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()