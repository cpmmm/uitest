# -*- coding: utf-8 -*-
'''
@time: 2020/1/5 0005 18:07
@author: chen
@contact: 1171954100@qq.com
@file: index_page.py
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
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from class_web_20190618.PO_V1.PageLocators.index_page_locator import IndexPageLocator as loc
from class_web_20190618.PO_V1.Common.basepage import BasePage
import time
from class_web_20190618.PO_V1.PageLocators.personal_page_locator import PersonalPageLocator as ppl

#首页
class IndexPage(BasePage):

    #检测元素是否存在
    def check_nick_name_exists(self):
        """
        :return:检测元素是否存在，存在返回True，不存在返回False
        """
        #等待，还不能把这两句合在一起写

        WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(loc.about_us_loc))

        #关于我们是在账户左边，有可能先出现，可以再做一次等待，等待0.5秒
        time.sleep(0.5)

        try:
            self.driver.find_element_by_xpath('//a[@href="/Member/index.html"]')
            return True
        except:
            return False


    #点击我的账户
    def click_my_account(self):
        self.click_element(loc.my_account_loc,"首页_点击我的账户")

    #点击页面标
    def select_frist_bid(self):
        self.click_element(loc.qtb_button_loc,"首页_点击页面中标")


