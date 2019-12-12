# -*- coding: utf-8 -*-
'''
@time: 2019/11/15 0015 11:19
@author: chen
@contact: 1171954100@qq.com
@file: test_case.py
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
'''为我们3-12号写的http_request 请求类，写4条用例，要求利用unittest进行单元测试 ，并且用老师教的3个方法 分别去加载用例执行
4条用例里面要求有2个正常用例 2个异常用例'''

import unittest
from Homework.homework_0321.http_requests import HttpReq

class TestAdd(unittest.TestCase):

    def test_normal_001(self):           #正常测试用例001
        '''正确用户名和正确密码，get请求'''
        login_url='http://192.168.30.128:8080/futureloan/mvc/api/member/login'   #请求地址
        method='get'                   #请求方式get
        param={'mobilephone': '15810901234', 'pwd': '123456'}    #手机号和密码
        expected='登录成功'                                   #期望值
        res=HttpReq().http_requests(login_url,method,param).json()  #实际值
        # res = HttpReq().http_requests(login_url, method, param)
        #断言
        self.assertEqual(expected,res['msg'])
        # self.assertEqual(expected, res)


    def test_normal_002(self):         #正常测试用例002
        '''正确用户名和密码，post请求'''
        login_url = 'http://192.168.30.128:8080/futureloan/mvc/api/member/login'
        method='post'
        param={'mobilephone': '15810901234', 'pwd': '123456'}
        expected='登录成功'
        res = HttpReq().http_requests(login_url, method, param).json()  # 实际值
        # res = HttpReq().http_requests(login_url, method, param)
        # 断言
        self.assertEqual(expected, res['msg'])
        # self.assertEqual(expected, res)

    #异常用例
    def test_abnormal_001(self):
        '''空用户名登录'''
        login_url = 'http://192.168.30.128:8080/futureloan/mvc/api/member/login'
        method = 'post'
        param ={'mobilephone': '', 'pwd': '123456'}
        expected = '手机号不能为空'
        res = HttpReq().http_requests(login_url, method, param).json()  # 实际值
        # res = HttpReq().http_requests(login_url, method, param)
        # 断言
        self.assertEqual(expected, res['msg'])
        # self.assertEqual(expected, res)

    def test_abnormal_002(self):
        '''空密码登录'''
        login_url = 'http://192.168.30.128:8080/futureloan/mvc/api/member/login'
        method = 'post'
        param = {'mobilephone': '15810901234', 'pwd': ''}
        expected = '密码不能为空'
        res = HttpReq().http_requests(login_url, method, param).json()  # 实际值
        # res = HttpReq().http_requests(login_url, method, param)
        # 断言
        self.assertEqual(expected, res['msg'])
        # self.assertEqual(expected, res)



