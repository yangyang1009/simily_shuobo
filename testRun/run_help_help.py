#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-04-06 10:44:34
# @Author  : Nxy
# @Site    : 
# @File    : run_help.py
# @Software: PyCharm
from selenium import  webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from testCase.models import myUnitFirefox

class RunHelp(myUnitFirefox.UnitFirefox):
    def __init__(self):
        pass

