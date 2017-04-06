#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-06 10:44:33
# @Author  : Nxy
# @Site    : 
# @File    : userVer.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from testCase.pageObj.basePage import BasePage
import time
from testCase.pageObj.basePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep
class UserVer(BasePage):
    #登录各个元素定位
    login_username_loc=(By.ID,"userid")
    login_password_loc=(By.ID,"password")
    login_button_loc=(By.XPATH,"/html/body/form/div[5]/div/div[1]/div[6]/input")
    user_login_success_href=(By.CSS_SELECTOR,"li.profile.single")
    #用户登陆后提示
    uname_error_remind_loc=(By.ID,"useridError")
    # 密码为空，密码用户名错误提示均使用这个
    pwd_error_remind_loc=(By.ID,"passwordError")
    user_login_success_loc=(By.XPATH,"/html/body/div[1]/div[5]/div/div[2]/div/span[1]")
    #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #进入论文检测服务
    enter_service_href=(By.ID,"navService")
    enter_service_name=(By.LINK_TEXT,"论文相似性检测")
    enter_org_service_name=(By.ID,"business")
    enter_shuobo_service_name=(By.CSS_SELECTOR,"div.panel-footer > button.btn.btn-primary")
    enter_shuobo_success="http://check.test.wanfangdata.com.cn/md/"
    enter_shuobo_fail="http://login.test.wanfangdata.com.cn/Login.aspx"

    def userLogin(self,username,password):
        '''
        用户登录
        :param username: 用户名
        :param password: 用户登录密码
        :return: 无返回值
        '''
        '''获取的用户名密码登录'''
        self.open("")
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(5)

    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)
    #登录密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)
    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #用户登录成功
    def user_login_success(self):
        self.find_element(*self.user_login_success_href).click()

    #用户名错误提示
    def uname_error_remind(self):
        return self.find_element(*self.uname_error_remind_loc).text
    #密码错误提示
    def pwd_error_remind(self):
        return self.find_element(*self.pwd_error_remind_loc).text
    #登录成功后显示的用户名
    def user_login_success_verify(self):
        return self.find_element(*self.user_login_success_loc).text

    def userEnterThurber(self):
        '''
        用户进入硕博论文检测服务
        :return:
        '''
        self.enter_serviceHref()
        sleep(1)
        self.enter_serviceName()
        sleep(1)
        self.enter_org_service()
        sleep(1)
        self.enter_shuobo_service()
        sleep(5)

    #进入服务选择
    def enter_serviceHref(self):
        self.find_element(*self.enter_service_href).click()
    #开始选择相似性检测
    def enter_serviceName(self):
        self.find_element(*self.enter_service_name).click()
    #鼠标悬停在机构专属服务处
    def enter_org_service(self):
        self.find_element(*self.enter_org_service_name).move_to_element()
    #选择硕博论文相似性检测
    def enter_shuobo_service(self):
        self.find_element(*self.enter_shuobo_service_name).click()

    def userLogout(self):

        pass
