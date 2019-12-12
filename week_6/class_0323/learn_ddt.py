# -*- coding: utf-8 -*-
'''
@time: 2019/11/14 0014 19:12
@author: chen
@contact: 1171954100@qq.com
@file: learn_ddt.py
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
#ddt  data driver test  数据驱动测试

#装饰器--->@staticmethod  @classmethod
import unittest
from ddt import ddt,data,unpack  #装饰器

@ddt        #装饰测试类  unittest.TestCase的子类
class TestAdd(unittest.TestCase):

    # @data(1,2,3,4,5)     #装饰方法  跟for循环一样，遍历每个数据，传递给被装饰的方法的参数，有几条数据  就执行几次用例
    # def test_001(self,a):
    #     print(a)

    # @data(*[[1,2],[3,4]])
    # @unpack
    # def test_001(self,a,b):
    #     print('a',a)
    #     print('b',b)

    #元组--->1个元素--->加*号--->元组里面变成2个元素
    # @data(*[{'a':0,'b':0,'expected':0},{'a':1,'b':1,'expected':2}])
    # @unpack  #对字典进行拆分（针对每一条用例的数据进行拆分）
    # def test_002(self,a,b,expected):   #如果是字典的话，要用它的key作为参数来进行数据接收
    #     print('a',a)
    #     print('b',b)
    #     print('expected',expected)


    #data里面数据传进来--元组，有1个元素，执行1条用例  [[0, 0, 0], [1, 1, 1]]
    #data数据加*号---变成了2个元素，执行2条用例  [0,0,0],[1,1,1]
    #加@unpack,根据逗号进行拆分，变成了3个参数---测试方法要用三个参数来进行接收
    # @data(*[[0,0,0],[1,2,3]])
    # @unpack
    # def test_003(self,a,b,c):
    #     print('a',a)
    #     print('b',b)
    #     print('c',c)


    #如果一个有3个参数，而另一个有4个参数，那么也得传4个参数进行接收，但是可以加None
    @data(*[[0,0,0],[1,2,3,4]])
    @unpack
    def test_004(self,a,b,c,d=None):
        print('a',a)
        print('b',b)
        print('c',c)
        print('d',d)
