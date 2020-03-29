# -*- coding: utf-8 -*-
'''
@time: 2020/1/5 0005 15:19
@author: chen
@contact: 1171954100@qq.com
@file: test_login_pytest.py
@desc:
        ┏┓　　　┏┓+ +
　　　┏┛┻━━━┛┻┓ + +
　　　┃　　　　　　　┃ 　
　　　┃　　　━　　　┃ ++ + + +
　　 ████━████ ┃+
　　　┃　　　　　　　┃ +
　　　┃　　　┻　　　┃
　　　┃　　　　　　　┃ + +
　　　┗━┓　　　┏━┛
　　　　　┃　　　┃　　　　　　　　　　　
　　　　　┃　　　┃ + + + +
　　　　　┃　　　┃　　　　Codes are far away from bugs with the animal protecting　　　
　　　　　┃　　　┃ + 　　　　神兽保佑,代码无bug　　
　　　　　┃　　　┃
　　　　　┃　　　┃　　+　　　　　　　　　
　　　　　┃　 　　┗━━━┓ + +
　　　　　┃ 　　　　　　　┣┓
　　　　　┃ 　　　　　　　┏┛
　　　　　┗┓┓┏━┳┓┏┛ + + + +
　　　　　　┃┫┫　┃┫┫
　　　　　　┗┻┛　┗┻┛+ + + +

'''
import unittest
from selenium import webdriver
import ddt

from class_web_20190618.PO_V1.PageObjects.login_page import LoginPage
from class_web_20190618.PO_V1.PageObjects.index_page import IndexPage
from class_web_20190618.PO_V1.TestDatas import login_datas as ld

from class_web_20190618.PO_V1.TestDatas import Comm_Datas as cd
import logging

from class_web_20190618.PO_V1.Common import logger

logger = logger.get_logger(__name__)

#用例三部曲：前置、步骤、断言
@ddt.ddt
class TestLogin(unittest.TestCase):

    #第一版
    # def setUp(self):
    #     #前置 - 启动浏览器，打开网页
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('{}/Index/login.html'.format(cd.base_url))
    #     self.driver.maximize_window()

    @classmethod
    def setUpClass(cls):
        #日志
        logger.info("准备测试前置")
        # 前置 - 启动浏览器，打开网页
        cls.driver = webdriver.Chrome()
        cls.driver.get('{}/Index/login.html'.format(cd.base_url))
        cls.driver.maximize_window()

    #第一版
    # def tearDown(self):
    #     self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        # 日志
        logger.info("准备测试后置")
        cls.driver.quit()


    def tearDown(self):
        self.driver.refresh()

    #正常用例   #登录+首页
    def test_login_2_success(self):
        logger.info("用例-正常场景-登录成功-使用到的测试数据")
        #步骤 - 登录操作 - 登录页面
        LoginPage(self.driver).login(ld.success_data["user"],ld.success_data["passwd"])     #测试对象+测试数据
        #断言 - 页面是否存在一个像我的账户之类的元素
        self.assertTrue(IndexPage(self.driver).check_nick_name_exists())   #测试对象+测试数据
        #断言 - url跳转
        #获取当前url网址 是 self.driver.current_url
        self.assertEqual(self.driver.current_url,ld.success_data["check"])   #测试对象+测试数据

    #异常用例-...     #可以对用例的运行顺序进行编号
    # @ddt.data(*ld.wrong_datas)
    # def test_login_0_failed_by_wrong_datas(self,data):
    #     logger.info("异常用例-表单错误信息-使用到的测试用例")
    #     # 步骤
    #     LoginPage(self.driver).login(data["user"],data["passwd"])
    #     # 断言
    #     self.assertEqual(data["check"],LoginPage(self.driver).get_error_msg_from_loginForm())
    #
    @ddt.data(*ld.fail_datas)
    def test_login_1_failed_by_fail_datas(self,data):
        logger.info("异常用例-页面中心错误信息-使用到的测试用例")
        # 步骤
        LoginPage(self.driver).login(data["user"],data["passwd"])
        #断言
        self.assertEqual(data["check"],LoginPage(self.driver).get_error_msg_from_pageCenter())



