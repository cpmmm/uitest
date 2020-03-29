# -*- coding: utf-8 -*-
'''
@time: 2020/2/27 0027 22:10
@author: chen
@contact: 1171954100@qq.com
@file: test_invest.py
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
#投标测试用例
import unittest
import ddt
from selenium import webdriver

from class_web_20190618.PO_V1.Common import logger
from class_web_20190618.PO_V1.TestDatas import Comm_Datas as cd
from class_web_20190618.PO_V1.TestDatas import login_datas as ld
from class_web_20190618.PO_V1.PageObjects.login_page import LoginPage
from class_web_20190618.PO_V1.PageObjects.index_page import IndexPage
from class_web_20190618.PO_V1.PageObjects.invest_page import InvestPage
from class_web_20190618.PO_V1.PageObjects.personal_page import PersonalPage
from class_web_20190618.PO_V1.TestDatas import invest_datas as invest_d


logger = logger.get_logger(__name__)

@ddt.ddt
class TestInvest(unittest.TestCase):

    #前置
    @classmethod
    def setUpClass(cls):
        logger.info("准备测试前置")
        #启动浏览器
        cls.driver = webdriver.Chrome()
        cls.driver.get('{}/Index/login.html'.format(cd.base_url))
        cls.driver.maximize_window()
        LoginPage(cls.driver).login(ld.success_data["user"],ld.success_data["passwd"])
        IndexPage(cls.driver).select_frist_bid()

        # 滚动条-将投标按钮置于页面底端
        ele = cls.driver.find_element_by_xpath('//button[@class="btn btn-special height_style"]')
        cls.driver.execute_script("arguments[0].scrollIntoView(false);", ele)


    #后置
    @classmethod
    def tearDownClass(cls):
        logger.info("准备测试后置")
        cls.driver.quit()

    #页面刷新
    def tearDown(self):
        self.driver.refresh()


    #正常测试用例
    def test_invest_2_success(self):
        logger.info("用例-正常场景-投资成功-使用到的测试数据")
        #步骤-投资操作-投资页面
        #滚动条
        ele = self.driver.find_element_by_xpath('//a[@href="/Member/index.html"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        #点击我的账户
        InvestPage(self.driver).click_my_account()
        #获取可用余额文本值
        PersonalPage(self.driver).get_old_available_balance()
        #点击首页
        PersonalPage(self.driver).click_index()
        #点击抢投标
        IndexPage(self.driver).select_frist_bid()
        #滚动条
        ele = self.driver.find_element_by_xpath('//button[@class="btn btn-special height_style"]')
        self.driver.execute_script("arguments[0].scrollIntoView(false);", ele)
        # 输入金额
        InvestPage(self.driver).bid_amount(invest_d.success_data["amount"])
        # 点击投标
        InvestPage(self.driver).click_bid()

        # # 点击查看并激活
        # InvestPage(self.driver).click_check_activate_button()
        # # 获取新的可用余额文本值
        # PersonalPage(self.driver).get_new_available_balance()

        #断言-判断check是否相等
        self.assertEqual(invest_d.success_data["check"],InvestPage(self.driver).get_success_msg_from_pageCenter())


    def test_invest_3_success(self):
        logger.info("用例-正常场景-投资成功-使用到的测试数据")
        # 步骤-投资操作-投资页面
        # 滚动条
        ele = self.driver.find_element_by_xpath('//a[@href="/Member/index.html"]')
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        # 点击我的账户
        InvestPage(self.driver).click_my_account()
        # 获取可用余额文本值
        old = PersonalPage(self.driver).get_old_available_balance().strip("元")

        # 点击首页
        PersonalPage(self.driver).click_index()
        # 点击抢投标
        IndexPage(self.driver).select_frist_bid()
        # 滚动条
        ele = self.driver.find_element_by_xpath('//button[@class="btn btn-special height_style"]')
        self.driver.execute_script("arguments[0].scrollIntoView(false);", ele)
        # 输入金额
        InvestPage(self.driver).bid_amount(invest_d.success_data["amount"])
        # 点击投标
        InvestPage(self.driver).click_bid()
        # 点击查看并激活
        InvestPage(self.driver).click_check_activate_button()
        # 获取新的可用余额文本值
        new = PersonalPage(self.driver).get_new_available_balance().strip("元")

        #断言金额是否相等
        self.assertEqual(float(new),float(old)-float(invest_d.success_data["amount"]))

    #异常测试用例-弹框信息比对
    @ddt.data(*invest_d.wrong_datas)
    def test_invest_0_failed_by_wrong_datas(self,data):
        logger.info("异常用例-弹框错误信息-使用到的测试用例")
        #步骤
        # 输入金额
        InvestPage(self.driver).bid_amount(data["amount"])
        # 点击投标
        InvestPage(self.driver).click_bid()
        #断言
        self.assertEqual(data["check"],InvestPage(self.driver).get_error_msg_from_pageCenter())

    @ddt.data(*invest_d.fail_datas)
    def test_invest_1_failed_by_wrong_datas(self,data):
        logger.info("异常用例-按钮文本错误信息-使用到的测试用例")
        #步骤
        #输入金额
        InvestPage(self.driver).bid_amount(data["amount"])
        #断言
        self.assertEqual(data["check"],InvestPage(self.driver).get_error_msg_from_button())
