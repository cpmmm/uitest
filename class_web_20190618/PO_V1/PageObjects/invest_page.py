# -*- coding: utf-8 -*-
'''
@time: 2020/2/27 0027 17:27
@author: chen
@contact: 1171954100@qq.com
@file: invest_page.py
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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from class_web_20190618.PO_V1.Common.basepage import BasePage
from class_web_20190618.PO_V1.PageLocators.invest_page_locator import InvestPageLocator as loc

#第一个标的页面
class InvestPage(BasePage):
    #检测页面元素是否存在
    def check_element_exists(self):
        """
        :return: 检测元素是否存在，是返回True，否则返回False
        """
        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.rztb_loc))

        try:
            self.driver.find_element_by_xpath('//div[text()="融资投标"]')
            return True
        except:
            return False

    #点击我的账户
    def click_my_account(self):
        self.click_element(loc.my_account_loc,"投资页面_点击我的账户")

    #输入投标金额
    def bid_amount(self,amount):
        self.input_text(loc.invest_amount_loc,"投资页面_输入投资金额",amount)

    #点击投标按钮
    def click_bid(self):
        self.click_element(loc.bid_button_loc,"投资页面_点击投标按钮")

    #点击查看并激活
    def click_check_activate_button(self):
        self.click_element(loc.check_activate_button,"投资页面_点击查看并激活按钮")

    #获取页面中间的正确信息-类似于弹出框
    def get_success_msg_from_pageCenter(self):
        #等待
        self.wait_eleVisible(loc.success_msg_from_pageCenter,"投资页面_弹框投资成功信息")
        return self.get_element_text(loc.success_msg_from_pageCenter,"投资页面_弹框投资成功信息")

    #获取页面中间的错误信息-类似于弹出框
    def get_error_msg_from_pageCenter(self):
        #等待
        self.wait_eleVisible(loc.error_notify_from_pageCenter,"投资页面_弹框投资错误信息")
        return self.get_element_text(loc.error_notify_from_pageCenter,"投资页面_弹框投资错误信息")

    #获取页面按钮错误文本信息
    def get_error_msg_from_button(self):
        self.wait_eleVisible(loc.error_notify_from_button,"投资页面_按钮错误文本信息")
        return self.get_element_text(loc.error_notify_from_button,"投资页面_按钮错误文本信息")

    #点击弹出框的查看并激活按钮
    def click_check_activate(self):
        self.click_element(loc.check_activate_button,"投资页面_查看并激活按钮")
