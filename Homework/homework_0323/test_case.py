# -*- coding: utf-8 -*-
'''
@time: 2019/11/15 0015 11:19
@author: chen
@contact: 1171954100@qq.com
@file: test_case.py
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
'''为我们3-12号写的http_request 请求类，写4条用例，要求利用unittest进行单元测试 ，并且用老师教的3个方法 分别去加载用例执行
4条用例里面要求有2个正常用例 2个异常用例'''

import unittest
from Homework.homework_0323.http_requests import HttpReq
from ddt import ddt,data,unpack


from Homework.homework_0323.param_data import param      #第二种方法


from Homework.homework_0323.xls import get_data_from_xls,write_result   #第三种方法

#共用的数据叫做共享变量 1.global  2.类
# class DoExcel:      #这个今天用不上，接口自动化用
# print(param)    #这是一个列表，但是@data需要的是一个元组

@ddt
class TestAdd(unittest.TestCase):
    #第一种data
    # @data(*[['http://192.168.30.128:8080/futureloan/mvc/api/member/login','get',
    #          {'mobilephone': '15810901234', 'pwd': '123456'},'登录成功'],
    #        ['http://192.168.30.128:8080/futureloan/mvc/api/member/login','post',
    #         {'mobilephone': '15810901234', 'pwd': '123456'},'登录成功'],
    #        ['http://192.168.30.128:8080/futureloan/mvc/api/member/login','post',
    #         {'mobilephone': '', 'pwd': '123456'},'手机号不能为空'],
    #        ['http://192.168.30.128:8080/futureloan/mvc/api/member/login','post',
    #         {'mobilephone': '15810901234', 'pwd': ''},'密码不能为空']])

    #def test_normal_001(self,param):   #一个参数的时候(param)，那么获得的是下面这个
    # ['http://192.168.30.128:8080/futureloan/mvc/api/member/login','get',
     # {'mobilephone': '15810901234', 'pwd': '123456'}]

    #第二种data
    # @data(*param)

    @data(*get_data_from_xls())
    @unpack             #根据逗号隔开
    def test_normal_001(self,login_url,method,param,expected,case_id):   #case_id是后加的，表示前两种用不到
        print('login_url是:{},method是:{},param是:{},expected是:{}'
              .format(login_url,method,param,expected))
        res=HttpReq().http_requests(login_url,method,param).json()
        #断言
        try:
            self.assertEqual(expected,res['msg'])
            print(res)
        except AssertionError as e:
            # raise e
            #测试不通过的结果，"failed" 写到excel
            row=int(case_id)+1                    #case_id是字符串，需要转成int类型
            write_result(row,'failed')

if __name__ == '__main__':
    unittest.main()






