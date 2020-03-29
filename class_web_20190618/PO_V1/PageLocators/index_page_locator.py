# -*- coding: utf-8 -*-
'''
@time: 2020/1/10 0010 16:38
@author: chen
@contact: 1171954100@qq.com
@file: index_page_locator.py
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

class IndexPageLocator:
    #首页中第三个标的抢投标按钮
    #/html/body/div[4]/div[1]/div[2]/div[1]/div[3]/div/a
    #/html/body/div[4]/div[1]/div[3]/div[1]/div[3]/div/a
    qtb_button_loc = (By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[1]/div[3]/div/a')

    #关于我们
    about_us_loc = (By.XPATH,'//a[text()="关于我们"]')

    #我的账户   //a[@href="/Member/index.html"]
    my_account_loc = (By.XPATH,'//a[@href="/Member/index.html"]')