# -*- coding: utf-8 -*-
'''
@time: 2019/12/3 0003 10:49
@author: chen
@contact: 1171954100@qq.com
@file: test_register.py
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
from API_7.common.http_request2 import HTTPRequest2
from API_7.common import do_excel
from API_7.common import contants
from ddt import ddt,data             #没导入ddt会执行一条结果
from API_7.common import do_mysql

@ddt
class TestRegister(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'TestRegister')
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        cls.http_request=HTTPRequest2()
        cls.mysql=do_mysql.DoMysql()

    @data(*cases)                    #data可以接收可迭代数据类型，列表，元组，字典
    def test_register(self,case):
        print(case.title)
        if case.data.find('register_mobile') > -1:
            sql='select max(mobilephone) from future.member'
            max_phone=self.mysql.fetch_one(sql)[0]          #查询最大手机号码

            #最大手机号码加1
            # max_phone=int(max_phone)+1    #因为库里最大是18999999999，所以这行被我注释
            print('最大手机号码',max_phone)

            #replace()方法是替换之后重新返回一个新的字符串，需要重新赋值给case.data
            case.data=case.data.replace('register_mobile',str(max_phone))      #最大手机号码替换参数值

        resp = self.http_request.request(case.method, case.url, case.data)

        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_result(case.case_id+1,resp.text,"pass")
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, "fail")
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
        cls.mysql.close()