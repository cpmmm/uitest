# -*- coding: utf-8 -*-
'''
@time: 2020/2/27 0027 22:01
@author: chen
@contact: 1171954100@qq.com
@file: invest_datas.py
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
from class_web_20190618.PO_V1.Common.dir_config import base_dir

#正常场景
success_data = {"amount":"100","check":"投标成功！"}

#异常场景
#出现类似弹出框的   请正确填写投标金额/投标金额必须为100的倍数
wrong_datas = [
    {"amount":"-100","check":"请正确填写投标金额"},
    {"amount":"110","check":"投标金额必须为100的倍数"},
    {"amount":"10","check":"投标金额必须为100的倍数"}
]

#按钮信息进行变化的  请输入10的整数倍
fail_datas = [
    {"amount":"100.01","check":"请输入10的整数倍"},
    {"amount":"99.99","check":"请输入10的整数倍"}
]