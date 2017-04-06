#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-06 10:44:33
# @Author  : Nxy
# @Site    : 
# @File    : run_userVer.py
# @Software: PyCharm

from HTMLTestRunner import  HTMLTestRunner
from testCase.models import myUnit
from testCase.models.userVer.userVer import UserVer
from testResult.getResultImage import getResultImage
import random
import time
import unittest
from time import sleep

class RunUserVer(myUnit.MyTest):
    def test_userLogout_run(self):
        pass
    def user_login_verify_run(self,username,password):
        '''
        用户登录用例运行
        :param username: 用户名
        :param password: 密码
        :return:
        '''
        UserVer(self.driver).userLogin(username,password)

    def test_login_success_run(self):
        '''用户名，密码正确'''
        self.user_login_verify_run(username="companyusers",password="f")
        sleep(2)
        userver=UserVer(self.driver)
        userver.user_login_success()
        self.assertEqual(userver.user_login_success_verify(),"companyusers服务站")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"user_pwd_true.jpg")
    def test_login_userpwdNull_run(self):
        '''用户名、密码为空登录'''
        time.sleep(2)
        self.user_login_verify_run("","")
        userver=UserVer(self.driver)
        self.assertEqual(userver.uname_error_remind(),"用户名不能为空")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"user_pwd_empty.jpg")
    def test_login_pwdNull_run(self):
        '''用户名正确，密码为空登录'''
        time.sleep(2)
        self.user_login_verify_run('companyusers',"")
        userver=UserVer(self.driver)
        self.assertEqual(userver.pwd_error_remind(),"密码不能为空")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"pwd_empty.jpg")
    def test_login_userNull_run(self):
        '''用户名为空，密码正确'''
        time.sleep(2)
        self.user_login_verify_run(username="",password="f")
        userver=UserVer(self.driver)
        self.assertEqual(userver.uname_error_remind(),"用户名不能为空")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uname_empty.jpg")
    def test_login_error_run(self):
        '''用户名与密码不匹配'''
        time.sleep(2)
        character=random.choice('123456rtyhj')
        username="companyusers"+character
        self.user_login_verify_run(username,"f")
        po=UserVer(self.driver)
        self.assertEqual(po.pwd_error_remind(),"用户名或密码不正确!")
        imagetest = getResultImage()
        imagetest.insert_image(self.driver,"uname_pwd_error.jpg")
    def test_userRegist_run(self):
        pass
    def test_forgetPwd_run(self):
        pass
if __name__=="__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    test_report_dir = '../testResult'
    test_case_run_dir ='../testRun'
    filename = test_report_dir+'/'+ now +'_result.html'
    discover_cases = unittest.defaultTestLoader.discover(test_case_run_dir,pattern='run_*.py',top_level_dir=None)
    fp= open(filename,'wb')
    print(filename)
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,title="测试报告",description="测试运行情况")
    runner.run(discover_cases) #运行测试用例
    fp.close()#关闭报告文件
    # unittest.main()


