import os
import unittest
#import HTMLTestRunner
import time
#from parameterized import parameterized
#from Readdata import as53data
from AS53pylib.lib import asweb


class AS53Web(unittest.TestCase):

    def setUp(self):
        print("Start Testing")
        print(os.path)

    def tearDown(self):
        print("Stop Testing")

    def test_TC0(self):
        asweb.asweb.loginprov(self,"47.11.1.5", "admin", "admin")
        print(os.environ['AS53_python'])
        time.sleep(3)

    def test_TC1(self):
        print("Finish")

