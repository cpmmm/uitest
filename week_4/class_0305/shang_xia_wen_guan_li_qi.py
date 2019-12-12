# -*- coding: utf-8 -*-
# @Time:2019/11/5 0005 11:24
# @Author:cp
# @Email:1171954100@qq.com
# @File:shang_xia_wen_guan_li_qi.py
# file=open("py15.txt",'w+',encoding='utf-8')
# file.write("今天演示失败")
# file.close()

with open('py15.txt','w+',encoding='utf-8') as file:
    file.write('今天不开心')
print(file.closed)

