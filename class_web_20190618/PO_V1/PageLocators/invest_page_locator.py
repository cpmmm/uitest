# -*- coding: utf-8 -*-
'''
@time: 2020/2/27 0027 17:30
@author: chen
@contact: 1171954100@qq.com
@file: invest_page_locator.py
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
from selenium.webdriver.common.by import By

class InvestPageLocator:
    #//div[text()="融资投标"]
    rztb_loc = (By.XPATH,'//div[text()="融资投标"]')

    #投资金额输入框   //input[@class="form-control invest-unit-investinput"]
    invest_amount_loc = (By.XPATH,'//input[@class="form-control invest-unit-investinput"]')

    #投标按钮     //button[text()="投标"]
    bid_button_loc = (By.XPATH,'//button[text()="投标"]')

    #提示框-页面中心正确的信息，类似于弹框
    #   //div[text()="投标成功！"]
    success_msg_from_pageCenter = (By.XPATH,'//div[text()="投标成功！"]')

    #提示框-页面中心错误的信息，类似于弹框
    #   //div[@class="text-center"]
    error_notify_from_pageCenter = (By.XPATH,'//div[@class="text-center"]')

    #提示框-查看并激活按钮
    #  //div[@class="layui-layer-content"]//button[text()="查看并激活"]
    check_activate_button = (By.XPATH,'//div[@class="layui-layer-content"]//button[text()="查看并激活"]')

    #提示框-关闭
    #  //a[@class="layui-layer-ico layui-layer-close layui-layer-close1"]
    close_loc = (By.XPATH,'//a[@class="layui-layer-ico layui-layer-close layui-layer-close1"]')

    #按钮错误文本信息   //button[@class="btn btn-special height_style"]
    error_notify_from_button = (By.XPATH,'//button[@class="btn btn-special height_style"]')

    # 我的账户   //a[@href="/Member/index.html"]
    my_account_loc = (By.XPATH, '//a[@href="/Member/index.html"]')



