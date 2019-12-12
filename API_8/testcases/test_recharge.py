# -*- coding: utf-8 -*-
'''
@time: 2019/11/29 0029 16:26
@author: chen
@contact: 1171954100@qq.com
@file: test_login.py
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
from API_8.common.http_request2 import HTTPRequest2
from API_8.common import do_excel
from API_8.common import contants
from ddt import ddt,data             #没导入ddt会执行一条结果,另外一定要把正常登录写在充值用例的第一条
from API_8.common.do_mysql import DoMysql

@ddt
class TestRecharge(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'TestRecharge')
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        cls.http_request=HTTPRequest2()
        cls.mysql = DoMysql()

    @data(*cases)                    #data可以接收可迭代数据类型，列表，元组，字典
    def test_recharge(self,case):
        print(case.title)

        #请求之前，判断是否需要执行sql
        if case.sql is not None:
            sql = eval(case.sql)['sql1']
            member = self.mysql.fetch_one(sql)
            print(member['LeaveAmount'])
            before = member['LeaveAmount']


        resp = self.http_request.request(case.method, case.url, case.data)
        actual_code=resp.json()['code']     #返回的是字典，然后找code，d[key]

        try:
            self.assertEqual(str(case.expected),actual_code)
            self.excel.write_result(case.case_id+1,resp.text,"pass")

            # 成功之后，判断是否需要执行sql
            if case.sql is not None:
                sql = eval(case.sql)['sql1']
                member = self.mysql.fetch_one(sql)
                print(member['LeaveAmount'])
                after = member['LeaveAmount']

                recharge_amount = int(eval(case.data)['amount'])   #充值金额
                self.assertEqual(before+recharge_amount,after)

        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, "fail")
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()