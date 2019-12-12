# -*- coding: utf-8 -*-
'''
@time: 2019/11/21 0021 11:17
@author: chen
@contact: 1171954100@qq.com
@file: send_email.py
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
#发送邮件
#自动化发邮件，首先要考虑手工怎么发送邮件
'''
1.选择邮件发送服务商，网易，qq等
2.登录
3.编写邮件
4.发送

#有很多协议，比如pop3,smtp
'''
#这个目前有问题,在配置文件那里有点问题
# import smtplib
# from week_7.class_0328.conf import email_name,email_pwd
# #选择邮件服务商
# server=smtplib.SMTP('smtp.163.com',25)
#
# #登录
# server.login(emailname,emailpwd)
#
# msg = '''\\
# From: chen
# Subject: testin'
#
# This is a test '''
#
# #发送邮件
# server.sendmail(emailname,'13716424686@163.com',msg)
# server.quit()


#上下文管理器
import smtplib
import ssl

context=ssl.create_default_context()

#加密  重要情报  tls 模式
with smtplib.SMTP('smtp.163.com',25) as server:
    server.login(emailname,emailpwd)
    server.starttls(context=context)      #加密
    msg = '''\\
    # From: chen
    # Subject: testin'
    #
    # This is a test '''

    server.sendmail(emailname,'13716424686@163.com',msg)


#加密  ssl  80--->443   邮件25---》465
with smtplib.SMTP_SSL('smtp.163.com',465) as server:
    server.login(emailname,emailpwd)
    server.starttls(context=context)      #加密
    msg = '''\\
    # From: chen
    # Subject: testin'
    #
    # This is a test '''

    server.sendmail(emailname,'13716424686@163.com',msg)

