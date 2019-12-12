# -*- coding: utf-8 -*-
'''
@time: 2019/11/10 0010 22:19
@author: chen
@contact: 1171954100@qq.com
@file: homework_0319.py
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
#写一个日志类
#结合配置文件 完成  输出的格式  输出级别的配置
import logging
class my_log:
    def __init__(self,file_name,level):
        self.file_name=file_name
        self.level=level

        # 新建一个日志收集器：getLogger()
        my_logger = logging.getLogger(file_name)  # 名为py15的日志收集器
        my_logger.setLevel(level)


        # 指定格式
        fmt = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-%(lineno)d-日志信息:%(message)s')

        # 新建指定的输出渠道
        # 指定输出渠道handler
        ch = logging.StreamHandler()  # 指定输出到console控制台
        ch.setLevel(level)  # 设定输出信息的级别
        ch.setFormatter(fmt)

        # 指定输出文本渠道
        file_handler = logging.FileHandler('py15.log', encoding='utf-8')
        file_handler.setLevel(level)
        file_handler.setFormatter(fmt)

        # 配合关系
        my_logger.addHandler(ch)
        my_logger.addHandler(file_handler)


if __name__ == '__main__':
        #收集日志
    pass


