#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-06 10:44:33
# @Author  : Cys
# @Site    :
# @File    : massProduceDeptStruc.py
# @Software: PyCharm
from testCase.pageObj.basePage import BasePage
from selenium.webdriver.common.by import By
import os
import time


class massProducePage(BasePage):
    """description of class"""

    #page element identifier
    buildDeptStructTab = (By.CSS_SELECTOR,'.navbar.navbar-inverse>div>div>ul>li:nth-child(1)')
    massProduceTab = (By.CSS_SELECTOR,'#listtab')
    downLoadtemplate = (By.CSS_SELECTOR,".help-block>a")
    massProduceButton = (By.CSS_SELECTOR,"#SWFUpload_0")

    #进入“建立院系结构>批量生成院系结构
    def toMassProducePage(self):
        buildDeptStructTab = self.driver.find_element(*massProducePage.buildDeptStructTab)
        buildDeptStructTab.click()
        massProduceTab = self.driver.find_element(*massProducePage.massProduceTab)
        massProduceTab.click()

    #下载院系结构模版
    def clickDownloadTemplate(self):
        downLoadtemplate  = self.driver.find_element(*massProducePage.downLoadtemplate)
        downLoadtemplate.click()

   #重命名就文件名，避免重复
    def renameFileName(self):
        name=time.strftime("%Y-%m-%d %H_%M_%S")
        #os.remove(r"F:\resultlog\SchoolStructrue.xlsx")
        os.rename(r"F:\resultlog\SchoolStructrue.xlsx",r"F:\resultlog\%s.xlsx"%(name))

    #判断是否下载到本地
    def verifyExist(self):
        os.path.exists(r"F:\resultlog\SchoolStructrue1.xlsx")