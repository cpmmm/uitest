# -*- coding: utf-8 -*-
'''
@time: 2019/12/21 0021 18:51
@author: chen
@contact: 1171954100@qq.com
@file: test_payment.py
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
'''
测试场景:
1.支付成功
2.支付失败
3.登录超时，成功
4.登录超时，失败
5.登录超时，超时
'''
import unittest
from API_Mock import payment
from unittest import mock

class PaymentTest(unittest.TestCase):

    def setUp(self):   #测试前置
        pass

    #测试场景
    #测试支付成功
    def test_success(self):
        pay = payment.Payment()
        mock.Mock(return_value=200)
        resp = pay.doPay(user_id=1,card_num="439019098",amount=200)
        self.assertEqual('success',resp)

    def tearDown(self):  #测试后置
        pass
