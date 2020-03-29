# -*- coding: utf-8 -*-
'''
@time: 2020/3/2 0002 11:02
@author: chen
@contact: 1171954100@qq.com
@file: personal_page.py
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
from class_web_20190618.PO_V1.PageLocators.personal_page_locator import PersonalPageLocator as loc

class PersonalPage(BasePage):
    #获取旧的可用金额文本值
    def get_old_available_balance(self):
        old_available_balance_text = self.get_element_text(loc.available_balance_loc,"个人页面_获取未投资时可用余额")
        return old_available_balance_text

    #点击首页
    def click_index(self):
        self.click_element(loc.index_loc,"个人页面_点击首页")


    #获取新的可用余额文本值
    def get_new_available_balance(self):
        new_available_balance_text = self.get_element_text(loc.available_balance_loc,"个人页面_获取投资后可用余额")
        return new_available_balance_text

