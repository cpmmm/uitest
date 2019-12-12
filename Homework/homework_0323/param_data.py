# -*- coding: utf-8 -*-
'''
@time: 2019/11/16 0016 14:26
@author: chen
@contact: 1171954100@qq.com
@file: param_data.py
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

'''这是一个起到配置作用的文件'''
param=[
           ['http://192.168.30.128:8080/futureloan/mvc/api/member/login','get',
             {'mobilephone': '15810901234', 'pwd': '123456'},'登录成功'],
           ['http://192.168.30.128:8080/futureloan/mvc/api/member/login','post',
            {'mobilephone': '15810901234', 'pwd': '123456'},'登录成功'],
           ['http://192.168.30.128:8080/futureloan/mvc/api/member/login','post',
            {'mobilephone': '', 'pwd': '123456'},'手机号不能为空'],
           ['http://192.168.30.128:8080/futureloan/mvc/api/member/login','post',
            {'mobilephone': '15810901234', 'pwd': ''},'密码不能为空']
    ]

#section,option,value
#[section]
#配置


# param=[
#     {'url':'http://192.168.30.128:8080/futureloan/mvc/api/member/login','method':'get',
#         'param':{'mobilephone': '15810901234', 'pwd': '123456'}},
#     {'url': 'http://192.168.30.128:8080/futureloan/mvc/api/member/login', 'method': 'post',
#      'param': {'mobilephone': '15810901234', 'pwd': '123456'}},
#     {'url': 'http://192.168.30.128:8080/futureloan/mvc/api/member/login', 'method': 'post',
#      'param': {'mobilephone': '', 'pwd': '123456'}},
#     {'url': 'http://192.168.30.128:8080/futureloan/mvc/api/member/login', 'method': 'post',
#      'param': {'mobilephone': '15810901234', 'pwd': ''}},
#       ]
