# -*- coding: utf-8 -*-
'''
@time: 2019/11/10 0010 22:21
@author: chen
@contact: 1171954100@qq.com
@file: learn_unittest.py
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
#主题：单元测试
#类：属性 方法
#属性  类属性  对象属性
#方法  类方法  静态方法   对象方法


#单元测试是谁做的？---开发和我都可以做

#单元测试是做什么？----对某个功能去做测试-->每一个功能是封装在类里面-->类里面有方法和属性

#单元测试测试什么？--->方法--->创建对象  调用方法  传参--->通过传递多组数据来测试不同的情况

#框架--->unittest--->pytest

#python----unittest   单元测试
#case-->TestCase
#suite-->TestSuite
#loader-->TestLoader
#runner-->TextTestResult  TextTeseRunner
#result-->TestResult

#写用例   case-->TestCase  用来写用例
import unittest
from week_6.class_0321.math_method import MathMethod

class TestAdd(unittest.TestCase):#测试类
    #没有测试用例--自己来加
    #测试用例：必须以test开头
    # def test_add_two_zero(self):         #测试2个0相加
    #     print('test_add_two_zero')
    #     expected = 0  # 期望值
    #     res = MathMethod().add(0,0)  # 实际值
    #     #断言
    #     self.assertEqual(expected,res)

    #改源码方案，不建议
    # def test_add_two_zero(self):
    #     print('a的值是{},b的值是{},expected的值是{}'.format(self.a,self.b,self.expected))
    #     res=MathMethod().add(self.a,self.b)#实际值
    #     #断言
    #     self.assertEqual(self.expected,res)

    def test_add_two_zero(self):
        print('a的值是{},b的值是{},expected的值是{}'.format(a,b,expected))
        res=MathMethod().add(a,b)#实际值
     #断言
        self.assertEqual(expected,res)


#     def test_add_positive_negative(self):  #测试一正一负数字相加
#         print('test_add_positive_negative')
#         expected = -2  # 期望值
#         res = MathMethod().add(1,-3)  # 实际值
#         # 断言
#         self.assertEqual(expected,res)
#
# class TestSub(unittest.TestCase):#测试类
#     #没有测试用例--自己来加
#     #测试用例：必须以test开头
#     def test_sub_two_zero(self):         #测试2个0相加
#         print('test_sub_two_zero')
#         expected=0                 #期望值
#         res=MathMethod().sub(0,0)  #实际值
#         #断言
#         self.assertEqual(expected,res)
#
#     def test_sub_positive_negative(self):  #测试一正一负数字相加
#         print('test_sub_positive_negative')
#         expected = 4  # 期望值
#         res = MathMethod().sub(1,-3)  # 实际值
#         # 断言
#         self.assertEqual(expected,res)


