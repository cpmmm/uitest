# -*- coding: utf-8 -*-
'''
@time: 2020/1/7 0007 15:22
@author: chen
@contact: 1171954100@qq.com
@file: login_page_locator.py
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
#登录页面元素定位

from selenium.webdriver.common.by import By

class LoginPageLocator:

    # 用户名输入框
    user_loc = (By.XPATH,'//input[@name="phone"]')

    #密码输入框
    passwd_loc = (By.XPATH,'//input[@name="password"]')

    #登录按钮
    login_button_loc = (By.TAG_NAME,"button")

    #提示框-登录表单区域
    error_notify_from_loginForm = (By.XPATH,'//div[@class="form-error-info"]')

    #提示框-页面中心错误信息
    error_notify_from_pageCenter = (By.XPATH,'//div[@class="layui-layer-content"]')
