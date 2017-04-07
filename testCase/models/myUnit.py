#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/3/13 13:25
# @Author  : Nxy
# @Site    : 
# @File    : MyUnit.py
# @Software: PyCharm
from browserDriver.setBrowser import setBrowser
import unittest
class MyTest(unittest.TestCase):
    def setUp(self):
        s= setBrowser()
        self.driver=s.startFirefox()
        #self.driver=s.startChrome("../browserDriver/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()


#
# if __name__=='__main__':
#     t = MyTest()
#     d = t.setUp()
#     d.get("http://www.baidu.com")

