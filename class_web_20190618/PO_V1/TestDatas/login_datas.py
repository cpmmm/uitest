# -*- coding: utf-8 -*-
'''
@time: 2020/1/6 0006 16:13
@author: chen
@contact: 1171954100@qq.com
@file: login_datas.py
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
from class_web_20190618.PO_V1.TestDatas.Comm_Datas import base_url
#测试数据

#正常场景
success_data = {"user":"13716424686","passwd":"chen123456",
                "check":"{}/Index/index".format(base_url)}

#异常
#密码为空/手机号为空/手机号格式不正确-少于11位/手机号格式不正确-大于11位
wrong_datas=[
    {"user":"18684720553","passwd":"","check":"请输入密码"},
    {"user":"","passwd":"python","check":"请输入手机号"},
    {"user":"1867744","passwd":"python","check":"请输入正确的手机号"},
    {"user":"186847055311","passwd":"python","check":"请输入正确的手机号"}
]

#用户名未注册/密码错误
fail_datas=[
    {"user":"18600000000","passwd":"python","check":"此账号没有经过授权，请联系管理员!"},
    {"user":"18684720553","passwd":"pyt","check":"帐号或密码错误!"}
]