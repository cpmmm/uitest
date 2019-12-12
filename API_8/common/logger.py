# -*- coding: utf-8 -*-
'''
@time: 2019/12/11 0011 10:01
@author: chen
@contact: 1171954100@qq.com
@file: logger.py
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
import logging
from API_8.common import contants

def get_logger(name):

    logger = logging.getLogger(name)
    logger.setLevel('DEBUG')

    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d]"
    formatter = logging.Formatter(fmt=fmt)

    console_handler = logging.StreamHandler()         #指定输出到控制台
    console_handler.setLevel('DEBUG')
    console_handler.setFormatter(formatter)

    #指定输出到log目录下,每次可以修改名称
    file_handler = logging.FileHandler(contants.log_dir+'/test_login.log',encoding='utf-8')
    file_handler.setLevel('INFO')
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

logger = get_logger('case')

# logger.info('测试开始啦！')
# logger.error('测试报错')       #控制台默认最低输出级别是error
# logger.debug('测试数据')
# logger.info('测试结束啦！')