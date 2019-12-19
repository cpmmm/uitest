# -*- coding: utf-8 -*-
'''
@time: 2019/12/11 0011 18:28
@author: chen
@contact: 1171954100@qq.com
@file: run.py
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
import sys

sys.path.append('./')   #project根目录地址
print(sys.path)

import unittest
import HTMLTestRunnerNew
from API_8.common import contants
# #第一种
# from API_8.testcases import test_register

# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
#
# #第一种
# suite.addTests(loader.loadTestsFromModule(test_register))

#第二种
discover = unittest.defaultTestLoader.discover(contants.case_dir,"test_*.py")

with open(contants.report_dir + '/report.html','wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title='python15 API test report',
                                              description='前程贷API',
                                              tester='chen')
    # runner.run(suite)

    runner.run(discover)