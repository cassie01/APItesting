import unittest
import sys
a = sys.path
b = "\n".join(a)
print(b)
# from web_automation.testcase import test01
from web_automation.0120.testcase import test01
import sys
def suite():
    suite = unittest.TestSuite()
    suite.addTest(test01.post_content('test_01_login'))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())

