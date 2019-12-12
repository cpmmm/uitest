# -*- coding: utf-8 -*-
# @Time:2019/10/31 0031 17:47
# @Author:cp
# @Email:1171954100@qq.com
# @File:neizhihanshu.py

#字符串
s="pythonyy"
# res=s.capitalize()       #首字母大写
# res=s.count("y",2,8)     #统计次数，取头不取尾
# res=s.find("y",2,8)      #找到子字符串第一次y出现的索引位置，可以限定位置，也可以没有限定位置，要是没找到就返回-1
# res=s.index("h")         #寻找字符串  并返回索引值  没找到就报错
# res=s.islower()          #判断字符串是否都是小写，都是的话返回True，否则返回False
# res=s.isupper()          #判断字符串是否都是大写，都是的话返回True，否则返回False
# res=s.upper()            #将字符串全部改成大写
# res=res.isupper()
# res=s.lower()            #将字符串全部改成小写
# res=res.islower()
# s=input("请输入数字")
# res=s.isdigit()          #判断是否是纯数字，不能有小数点，有小数点返回false，否则返回true
# s=input("请输入数字")
# res=s.isdecimal()        #判断数字是否是纯十进制数字，是返回true，否则返回false  十进制就是阿拉伯数字
res='$'.join(s)          #join表示拼接，拼接对象是可迭代的数据类型，比如字符串，列表，元组，字典

print(res)