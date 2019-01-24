import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
sys.path.append(current_dir)
sys.path.append("..")
from element import BasePageElement

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'span>  a.dark'

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    def __init__(self, driver, username, psw,url ):
        """
        定义需要的参数，后面需要传参的参数
        """
        self.driver = driver
        self.username = username
        self.psw = psw
        self.url = url


    def login(self):
        """
        用户登录操作
        """
        self.driver.get('http://39.107.96.138:3000/signin')
        self.driver.find_element_by_id('name').send_keys(self.username)
        self.driver.find_element_by_id('pass').send_keys(self.psw)
        self.driver.find_element_by_class_name('span-primary').click()

    def is_login_success(self):
        pass

    def get_login_name(self):
        """获取username"""

        # username = self.driver.find_element_by_css_selector('span>  a.dark').text
        return SearchTextElement()

    def is_url_success(self):
        url = self.driver.current_url
        print(url)
        return url