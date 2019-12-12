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
from ddt import ddt,data             #没导入ddt会执行一条结果，然而写了6条
from API_8.common import logger


logger = logger.get_logger(__name__)

@ddt
class TestLogin(unittest.TestCase):
    excel = do_excel.DoExcel(contants.case_file, 'TestLogin')
    cases = excel.get_case()

    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置')
        cls.http_request=HTTPRequest2()

    @data(*cases)                    #data可以接收可迭代数据类型，列表，元组，字典
    def test_login(self,case):
        # print(case.title)

        logger.info('开始测试:{0}'.format(case.title))
        resp = self.http_request.request(case.method, case.url, case.data)

        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_result(case.case_id+1,resp.text,"pass")
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1, resp.text, "fail")
            logger.error('测试报错了,{0}'.format(e))
            raise e

        logger.info('结束测试:{0}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()