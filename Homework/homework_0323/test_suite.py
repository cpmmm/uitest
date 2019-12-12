# -*- coding: utf-8 -*-
'''
@time: 2019/11/15 0015 16:15
@author: chen
@contact: 1171954100@qq.com
@file: test_suite.py
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
import HTMLTestRunnerNew
from Homework.homework_0323.test_case import *

suite=unittest.TestSuite()     #创建一个对象

#第一种方法，一个一个去添加用例
# suite.addTest(TestAdd('test_normal_001'))
# suite.addTest(TestAdd('test_normal_002'))
# suite.addTest(TestAdd('test_abnormal_001'))
# suite.addTest(TestAdd('test_abnormal_002'))

#第二种方法：通过loader来加载用例  通过模块加载用例
# from Homework.homework_0321 import test_case
# loader=unittest.TestLoader()     #用例加载器
# suite.addTest(loader.loadTestsFromModule(test_case))

#第三种方法:通过loader来加载用例，通过测试类名来加载用例
from Homework.homework_0323.test_case import *
loader=unittest.TestLoader()       #用例加载器
suite.addTest(loader.loadTestsFromTestCase(TestAdd))

# #执行用例--unittest版本
# with open('test.txt','w',encoding='utf-8') as file:
#     runner=unittest.TextTestRunner(stream=file,verbosity=2)   #创建一个对象来执行用例
#     runner.run(suite)

# #执行并生成html测试报告
with open('test.html','wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(
        stream=file,
        verbosity=2,
        title='20190323测试报告',
        description='作业0321基础改写',
        tester='chenpeng')

    runner.run(suite)


#测试流程：设计测试用例：url...method...data...预期结果
#1.excel
#2.配置文件  ini，conf，propties
#3.txt
#4.变量
