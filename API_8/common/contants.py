# -*- coding: utf-8 -*-
'''
@time: 2019/11/29 0029 10:29
@author: chen
@contact: 1171954100@qq.com
@file: contants.py
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

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #API_4
# print(base_dir)

case_file=os.path.join(base_dir,'data','TestRegister.xlsx')
# print(case_file)

global_file=os.path.join(base_dir,'config','global.conf')
# print(global_file)

online_file=os.path.join(base_dir,'config','online.conf')
# print(online_file)

test_file=os.path.join(base_dir,'config','test.conf')
# print(test_file)

log_dir = os.path.join(base_dir,'log')

case_dir = os.path.join(base_dir,'testcases')

report_dir = os.path.join(base_dir,'reports')