# -*- coding: utf-8 -*-
'''
@time: 2019/12/5 0005 10:37
@author: chen
@contact: 1171954100@qq.com
@file: test_add.py
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
import unittest
from API_6.common.http_request2 import HTTPRequest2
from API_6.common import do_excel
from API_6.common import contants
from ddt import ddt,data             #没导入ddt会执行一条结果
from API_6.common.config import config
from API_6.common import context

@ddt
class TestAdd(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'TestAdd')
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        cls.http_request=HTTPRequest2()

    @data(*cases)                    #data可以接收可迭代数据类型，列表，元组，字典
    def test_add(self,case):
        print(case.title)

        # case.data=eval(case.data)    #变成字典
        #
        # if case.data.__contains__('mobilephone') and case.data['mobilephone'] == 'normal_user':
        #     case.data['mobilephone'] = config.get('data','normal_user')       #拿到配置文件里面的值赋值给mobilephone
        #
        # if case.data.__contains__('pwd') and case.data['pwd'] == 'normal_pwd':
        #     case.data['pwd'] = config.get('data','normal_pwd')
        #
        # if case.data.__contains__('memberId') and case.data['memberId'] == 'loan_member_id':
        #     case.data['memberId'] = config.get('data','loan_member_id')

        #在请求之前替换参数化的值
        case.data = context.replace(case.data)

        resp = self.http_request.request(case.method, case.url, case.data)
        print(resp.text)
        print(resp.status_code)

        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_result(case.case_id+1,resp.text,"pass")
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, "fail")
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()