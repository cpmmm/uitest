# -*- coding: utf-8 -*-
'''
@time: 2020/1/5 0005 14:24
@author: chen
@contact: 1171954100@qq.com
@file: login_page.py
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
from selenium.webdriver.common.by import By
import time

from class_web_20190618.PO_V1.PageLocators.login_page_locator import LoginPageLocator as loc

from class_web_20190618.PO_V1.Common.basepage import BasePage
#登录页面
#一个用例，一次浏览器的打开和关闭
class LoginPage(BasePage):      #继承一下

    # 登录功能
    def login(self,user,passwd):
        self.input_text(loc.user_loc,"登录页面_输入用户名",user)
        self.input_text(loc.passwd_loc,"登录页面_输入密码",passwd)
        self.click_element(loc.login_button_loc,"登录页面_点击登录按钮")


    #获取表单登录错误信息
    #  //div[@class="form-error-info"]
    def get_error_msg_from_loginForm(self):
        #等待
        self.wait_eleVisible(loc.error_notify_from_loginForm,"登录页面_表单区域错误信息")
        return self.get_element_text(loc.error_notify_from_loginForm,"登录页面_表单区域错误信息")

    #获取页面中间错误信息
    #//div[@class="layui-layer-content"]
    def get_error_msg_from_pageCenter(self):
        #等待
        self.wait_eleVisible(loc.error_notify_from_pageCenter,"登录页面_页面中心错误信息")
        return self.get_element_text(loc.error_notify_from_pageCenter,"登录页面_页面中心错误信息")