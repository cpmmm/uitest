# -*- coding: utf-8 -*-
'''
@time: 2020/1/12 0012 15:18
@author: chen
@contact: 1171954100@qq.com
@file: main.py
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
# 记录一下用例的执行过程 - 日志
# 如果用例失败 - Trackback报错信息 - 失败了截图
# 记录一下用例的运行时间 - 起始 - 等待的时候 - 等待时长

# 用例、页面对象当中。用例 - 页面对象 + 测试数据
#断言失败了！或页面对象执行的时候，报错了！

#页面对象 - 任意功能 = 等待元素可见、等待元素存在、点击、输入、文本获取、属性获取、alert切换、iframe切换、下拉列表、上传。。。


import sys
import unittest
import HTMLTestRunnerNew
from class_web_20190618.PO_V1.Common import dir_config

sys.path.append('./')
# print(sys.path)

discover = unittest.defaultTestLoader.discover(dir_config.testcases_dir,"test_login.py")

with open(dir_config.htmlreport_dir + '/report.html','wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              title='python15 API test report',
                                              description='前程贷UI',
                                              tester='chen')
    runner.run(discover)
