from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
import logging

# FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
# logging.basicConfig(format=FORMAT)
# d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
# logging.warning('Protocol problem: %s', 'connection reset', extra=d)

FORMAT = '%(asctime)-15s %(message)s %(action)s'
logging.basicConfig(filename='example.log',filemode = 'w', format=FORMAT, level=logging.DEBUG)
d = {'action' : 'test for 001'}

# driver = webdriver.Chrome()
# logging.debug('debug error: %s', extra = d)
logging.warning('error : %s',extra = d )
logging.info('info1111 : %s',extra = d)


# class post_content(unittest.TestCase):
    
   
#     def test_01_login(self):
#         # driver = self.driver
#         # d = {'clientip': '9.9.9.9', 'user': 'xd'}
#         # logging.warning('Protocol problem: %s', 'connection time out', extra=d)
#         # logging.warning('This message should go to the log file')
#         # logging.info('So should this')
#         # logging.warning('And this, too')
#         driver.get('https://baidu.com')


# if __name__ == "__main__":
#     unittest.main(verbosity =2)



