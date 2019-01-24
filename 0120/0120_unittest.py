from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains

# driver = webdriver.Chrome()
class post_content(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        pngname = time.strftime("%b %d %Y %H:%M:%S", time.gmtime())
        cls.driver.save_screenshot(pngname+'.png')
        # print('pinduoduo')

    # def setUp(self):
    #     # self.driver = webdriver.Chrome()
    #     print('121212')

    def test_01_login(self):
        driver = self.driver
        driver.get('http://39.107.96.138:3000/signin')
        driver.find_element_by_id('name').send_keys('user1')
        driver.find_element_by_id('pass').send_keys('123456')
        driver.find_element_by_class_name('span-primary').click()

        url = driver.current_url
        self.assertEqual(url, "http://39.107.96.138:3000/")
        name = driver.find_element_by_css_selector(' div.user_card > div> span.user_name > a').text
        self.assertEqual(name, "user1")

    @unittest.skip('neednot do it')
    def test_02_post(self):
        driver = self.driver
        driver.get('http://39.107.96.138:3000/topic/create')
        driver.find_element_by_id('tab-value').click()
        driver.find_element_by_css_selector('#tab-value > option:nth-child(2)').click()
        driver.find_element_by_name('title').send_keys('0201')
        content = driver.find_element_by_class_name('CodeMirror-scroll')
        content.click()
        ActionChains(driver).move_to_element(content).send_keys("it's time !!").perform()
        driver.find_element_by_class_name('submit_btn').click()

    # def tearDown(self):
    #     driver.quit()
    #     print('343434')

    @classmethod
    def tearDownClass(cls):
        driver = cls.driver
        print('wahahah')
        driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity =2)



