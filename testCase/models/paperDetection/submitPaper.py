#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-06 10:44:33
# @Author  : Nxy
# @Site    : 
# @File    : submitPaper.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from testCase.pageObj.basePage import BasePage
from selenium.webdriver.common.by import By
from testCase.models.paperDetection.paperDetectObj import PaperDetectObj
import time

class SubmitPaper(BasePage):
    '''
    硕博 论文检测中上传论文功能测试用例
    '''

    local_upload_butn_element = (By.ID,"userid")
    add_folder_checkbox_element = ()
    add_folder_alter_element = ()
    add_folder_new_element = ()
    add_folder_old_element = ()
    add_folder_input_element = ()
    add_folder_select_element = ()
    add_folder_sumit_element = ()
    add_folder_cancle_element = ()
    start_check_butn_element = ()
    #用户单篇上传
    def simple_upload_paper(self,username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)
    #用户选择论文上传功能
    def login_username(self,username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)





    def addFolder(self):
        pass
    def startTest(self):
        pass
    def deletePaper(self):
        pass
    def transferSubAccount(self):
        pass
    def checkFolderList(self):
        pass
