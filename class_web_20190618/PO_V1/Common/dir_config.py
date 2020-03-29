# -*- coding: utf-8 -*-
'''
@time: 2020/1/12 0012 18:39
@author: chen
@contact: 1171954100@qq.com
@file: dir_config.py
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
import os

#框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
# print(base_dir)

testdatas_dir = os.path.join(base_dir,"TestDatas")

testcases_dir = os.path.join(base_dir,"TestCases")

htmlreport_dir = os.path.join(base_dir,"Outputs/reports")

logs_dir = os.path.join(base_dir,"Outputs/logs")

screenshot_dir = os.path.join(base_dir,"Outputs/screenshots")
# print(screenshot_dir)