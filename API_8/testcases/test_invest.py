# -*- coding: utf-8 -*-
'''
@time: 2019/12/7 0007 14:54
@author: chen
@contact: 1171954100@qq.com
@file: test_invest.py
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
from ddt import ddt,data             #没导入ddt会执行一条结果
from API_8.common.config import config
from API_8.common import context
from API_8.common import do_mysql
from API_8.common.context import Context

@ddt
class TestInvest(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'TestInvest')
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        cls.http_request=HTTPRequest2()
        cls.mysql = do_mysql.DoMysql()

    @data(*cases)                    #data可以接收可迭代数据类型，列表，元组，字典
    def test_invest(self,case):
        print(case.title)


        #在请求之前替换参数化的值
        case.data = context.replace(case.data)

        resp = self.http_request.request(case.method, case.url, case.data)
        print(resp.text)
        print(resp.status_code)

        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_result(case.case_id+1,resp.text,"pass")

            #判断加标之后，查询数据库，取到loan_id
            if resp.json()['msg'] == "加标成功":
                sql ='select id from future.loan where memberId = 1197 ORDER BY id desc limit 1;'
                loan_id = self.mysql.fetch_one(sql)[0]        #fetch_one返回的是元组
                print("标的id是:",loan_id)

                #保存到类属性里面
                setattr(Context,"loan_id",str(loan_id))

        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, "fail")
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()