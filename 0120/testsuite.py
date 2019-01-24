import unittest
from testcase import test01
import sys
def suite():
    suite = unittest.TestSuite()
    suite.addTest(test01.post_content('test_01_login'))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())
# a = sys.path
# b = "\n".join(a)
# print(b)
