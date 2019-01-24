import unittest
import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)
sys.path.append("..")
from page import LoginPage
from selenium import webdriver
"""手动添加目录，导入其他文件中的类
"""

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_login(self):
        username = 'user1'
        psw = '123456'
        url = "http://39.107.96.138:3000/"
        #向类中传入需要的三个参数
        lg = LoginPage(self.driver, username, psw, url)
        lg.login()
        # result_username = lg.get_login_name()
        # self.assertEqual(result_username, username)
        c_url = lg.is_url_success()
        # print(url)
        self.assertEqual(c_url, url)

    def tearDown(self):
        pass

    
    
