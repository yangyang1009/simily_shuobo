#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/4/7 14:38
# @Author  : Nxy
# @Site    : 
# @File    : paperDetectObj.py
# @Software: PyCharm
from testCase.pageObj.basePage import BasePage
from selenium.webdriver.common.by import By
class PaperDetectObj(BasePage):
    paper_check_menu_element = (By.LINK_TEXT,"论文检测") #论文检测菜单
    upload_paper_tab_element = (By.ID,"up_move") #上传论文
    handmade_paper_tab_element= (By.ID,"movein") #手工录入
    #用户进入论文检测菜单
    def enter_paper_detect(self):
        self.find_element(*self.paper_check_menu_element).click()

    #用户选择论文上传
    def select_upload_paper(self):
        self.find_element(*self.upload_paper_tab_element).click()

    #用户选择手工录入
    def select_handmade_paper(self):
        self.find_element(*self.handmade_paper_tab_element).click()

