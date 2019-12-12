# -*- coding: utf-8 -*-
'''
@time: 2019/11/21 0021 22:10
@author: chen
@contact: 1171954100@qq.com
@file: d3.email.py
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
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart    #很多不同部分

from email.mime.application import MIMEApplication         #传附件

#总的邮件内容，分为不同的模块
msg_total=MIMEMultipart()
msg_total['Subject']="hello"

#正文模块
msg_raw="""<p style="color:red">你好</p>
"""

msg=MIMEText(msg_raw,'html')
msg_total.attach(msg)

#附件模块
file=MIMEApplication(open('demo.txt','rb').read())
#添加附件的头信息
file.add_header('Content-Dispostion','attachment',filename='demo.txt')
#附件模块添加到总的里面
msg_total.attach(file)

with smtplib.SMTP_SSL('smtp.163.com',465) as server:
    server.login(emailname,emailpwd)
    server.starttls(context=context)      #加密
    # msg = '''\\
    # From: chen
    # Subject: testin'
    #
    # This is a test '''

    server.sendmail(emailname,'13716424686@163.com',msg_total.as_string())