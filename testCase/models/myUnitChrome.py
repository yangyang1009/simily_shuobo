#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/7 17:48
# @Author  : Nxy
# @Site    : 
# @File    : myUnitChrome.py
# @Software: PyCharm
from browserDriver.setBrowser import setBrowser
import unittest
class UnitChrome(unittest.TestCase):
    def setUp(self):
        s= setBrowser()
        self.driver=s.startChrome("../browserDriver/chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()


#
# if __name__=='__main__':
#     t = UnitChrome()
#     d = t.setUp()
#     d.get("http://www.baidu.com")

