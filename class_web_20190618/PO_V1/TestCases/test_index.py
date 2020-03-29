# -*- coding: utf-8 -*-
'''
@time: 2020/1/8 0008 10:22
@author: chen
@contact: 1171954100@qq.com
@file: test_index.py
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
#测试三部曲：前置，步骤(用户页面操作)，断言(页面操作)

#前置
"""
1.投资账号登录
2.要有可投的标-有可投余额。没有就加标-从接口
3.用户余额充足 - 充值5000 -- 接口实现
             - 钱>投资金额  不充。不大于呢？一口气冲2000000
             -开始就一次性冲很多
"""

"""
用例1：正常投资，投资金额1000
异常用例：
    1）投资金额为10，提示：投标金额必须为100的倍数
    2）投资金额为12，提示：请输入10的整数倍
    3）投资为非数字1-，提示：请输入10的整数倍
    4）投资为0/负数/为空，提示：请正确填写投标金额
    
    5）投资数 > 标总投资额，提示：购买标的金额不能大于标剩余金额
        #充值10万，创建一个借款9万的标
        
    6）投资数 > 账户可用余额 且 标可投 > 投资数 提示：购买标的金额不能大于标剩余金额 
        #投资数20w，但是账户只有10w，标可投200w
        
    7）含有空格，如1 00，提示：请输入10的整数倍
"""

#步骤
"""
1.首页--选一个标，进入投标页面
2.投资页面--输入金额，进行投资
"""

#断言
"""
1.个人页面-个人余额少的部分 == 投资前的金额-投资后的金额
2.投资记录
3.标的可投金额-投资金额 = 投资之后的金额
"""

import unittest
import ddt
from selenium import webdriver

from class_web_20190618.PO_V1.PageObjects.login_page import LoginPage
from class_web_20190618.PO_V1.PageObjects.index_page import IndexPage
from class_web_20190618.PO_V1.TestDatas import login_datas as ld
from class_web_20190618.PO_V1.TestDatas import Comm_Datas as cd
from class_web_20190618.PO_V1.TestDatas import index_datas as index_d
from class_web_20190618.PO_V1.PageObjects.invest_page import InvestPage
from class_web_20190618.PO_V1.PageObjects.personal_page import PersonalPage
from class_web_20190618.PO_V1.Common import logger

logger = logger.get_logger(__name__)

#用例三部曲：前置、步骤、断言
@ddt.ddt
class TestIndex(unittest.TestCase):

    #前置
    @classmethod
    def setUpClass(cls):
        # 日志
        logger.info("准备测试前置")
        # 前置 - 启动浏览器，打开网页
        cls.driver = webdriver.Chrome()
        cls.driver.get('{}/Index/login.html'.format(cd.base_url))
        cls.driver.maximize_window()
        LoginPage(cls.driver).login(ld.success_data["user"],ld.success_data["passwd"])


    #后置
    @classmethod
    def tearDownClass(cls):
        # 日志
        logger.info("准备测试后置")
        cls.driver.quit()

    # #正常用例
    def test_index_success(self):
        logger.info("用例-正常场景-点击第一个投标-使用到的测试数据")
        #步骤-首页 - 点击我的账户
        # IndexPage(self.driver).click_my_account()
        # #步骤-个人页面 - 获取可用余额
        # PersonalPage(self.driver).get_old_available_balance()
        # #步骤-个人页面 - 点击首页
        # PersonalPage(self.driver).click_index()
        #步骤-首页 - 选取页面标进行投资
        IndexPage(self.driver).select_frist_bid()

        #断言-页面是否存在融资投标这个元素
        self.assertTrue(InvestPage(self.driver).check_element_exists())







        #获取个人余额，获取当前标的可投金额
        #标页面 - 获取用户余额，获取标的可投金额
        #标页面 - 投资2000
        #标页面 - 弹出框
        #断言
        #投资金额 = 投资前的钱 - 投资后的钱
        #个人页面 - 获取投资后的可用余额
        #标页面 - 获取投资后的标的可投金额



    #异常用例
    # def test_invest_failed_wrong_format(self):
    #     # 步骤
    #     # 首页 - 选标进行投资
    #     # 获取个人余额，获取当前标的可投金额
    #     # 标页面 - 获取用户余额，获取标的可投金额
    #     # 标页面 - 投资操作
    #     #断言
    #     #提示信息对不对？
    #     #个人钱有没有少？
    #
    #     pass