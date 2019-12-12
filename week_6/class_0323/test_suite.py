# -*- coding: utf-8 -*-
'''
@time: 2019/11/11 0011 11:19
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
from week_6.class_0321.learn_unittest import *
import HTMLTestRunnerNew          #HTMLTestRunnerNew.py文件放在了C盘，python34里的lib文件夹下
#因为代码里有两个类，所以是from week_6.class_0321.learn_unittest import * ，*号是所有

#存储用例的容器 suite 套件
suite=unittest.TestSuite()   #创建一个对象

# 第一种方法：一个一个的去添加用例
# suite.addTest(TestAdd('test_add_two_zero'))     #添加测试用例到suite这个套件里面  用例是测试类的实例
# suite.addTest(TestAdd('test_add_positive_negative'))

# suite.addTest(TestAdd('test_add_two_zero'))
# suite.addTest(TestAdd('test_add_two_zero'))
# suite.addTest(TestAdd('test_add_two_zero'))

#第二种方法：通过loader来加载用例  通过模块加载用例
# from week_6.class_0321 import learn_unittest
# loader=unittest.TestLoader()      #用例加载器
# suite.addTest(loader.loadTestsFromModule(learn_unittest))

#第三种方法：通过loader来加载用例，通过测试类名来加载用例
# from week_6.class_0321.learn_unittest import *
# loader=unittest.TestLoader()         #用例加载器
# suite.addTest(loader.loadTestsFromTestCase(TestSub))


# #执行用例--unittest版本
# with open('test.txt','w') as file:
#     runner=unittest.TextTestRunner(stream=file,verbosity=2)#创建一个对象来执行用例
#     runner.run(suite)

#执行并生成html测试报告--HTMLTestRunnerNew
with open('test.html','wb') as file:
     runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,verbosity=2,
                                             title='20190323py15测试报告',
                                             description='加法减法功能验证',
                                             tester='cp')#创建一个对象来执行用例
     runner.run(suite)

#  . 通过了一条用例，通过了几条就有几个点   E代码出错  F用例执行失败