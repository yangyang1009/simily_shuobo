#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-06 10:44:33
# @Author  : Cys
# @Site    :
# @File    : run_massProduceDeptStruc.py
# @Software: PyCharm
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from testCase.models import myUnitChrome
from browserDriver.setBrowser import setBrowser
from testCase.models.buildDeptStruc.massProduceDeptStruc import massProducePage
from testCase.models.userVer.userVer import UserVer
from time import sleep
from testResult.getResultImage import getResultImage


class RunMassProduceDeptStruc(myUnitChrome.UnitChrome):
    def user_login(self):
        '''用户登录'''
        user_login = UserVer(self.driver)
        user_login.userLogin(username="companyusers",password="f")

    def atest_massProduceDeptStruc_run(self):
        pass
    def test_downloadTemplate_run(self):
        '''点击下载模版，文件下载至本地'''
        self.user_login()
        sleep(2)
        mass_page = massProducePage(self.driver)
        mass_page.toMassProducePage()
        mass_page.renameFileName()
        mass_page.clickDownloadTemplate()
        time.sleep(10)
        mass_page.verifyExist()
        #imagetest = getResultImage()
        #imagetest.insert_image(self.driver,"pwd_exist.jpg")
    def atest_checkDeptStrucList_run(self):
        pass

if __name__ == "__main__":
    unittest.main()