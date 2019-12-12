# -*- coding: utf-8 -*-
'''
@time: 2019/11/10 0010 15:54
@author: chen
@contact: 1171954100@qq.com
@file: learn_log.py
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
#日志：记录程序代码，操作
#主要目的  我们要写一个我们自己的日志类
#logging  来写日志模块
#不能用关键字，自带模块和第三方模块当文件名
#log也有等级：debug--》info--》warning--》error--》critical/fatal   从左到右越来越严重

#日志：收集5条，输出3条，输出有区别，只输出info以上级别

#收集--》日志收集器  root 默认
#输出--》输出渠道1）控制台console   2）指定文件 file  默认的是console
#默认  只输出info以上级别

import logging

#新建一个日志收集器：getLogger()

my_logger=logging.getLogger('py15')    #名为py15的日志收集器
my_logger.setLevel("DEBUG")            #设定收集的级别

#指定格式
fmt=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-%(lineno)d-日志信息:%(message)s')

#新建指定的输出渠道
#指定输出渠道handler
ch=logging.StreamHandler()    #指定输出到console控制台
ch.setLevel('DEBUG')          #设定输出信息的级别
ch.setFormatter(fmt)

#指定输出文本渠道
file_handler=logging.FileHandler('py15.log',encoding='utf-8')
file_handler.setLevel('DEBUG')
file_handler.setFormatter(fmt)

#配合关系
my_logger.addHandler(ch)
my_logger.addHandler(file_handler)

#收集日志
my_logger.debug('this is a debug msg')
my_logger.info('this is a info msg')
my_logger.warning('this is a warning msg')
my_logger.error('this is a error msg')
my_logger.critical('this is a critical msg')

#写一个日志类
#结合配置文件 完成  输出的格式  输出级别的配置
