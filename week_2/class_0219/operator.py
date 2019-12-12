# -*- coding: utf-8 -*-
# @Time:2019/10/29 0029 11:09
# @Author:cp
# @Email:1171954100@qq.com
# @File:operator.py


#operator:运算符
#算数运算符：+ - * /  %：取模，就是取余数  //：地板除，就取整数，小数不要
# a=10
# b=3
# c=0.2
# d=0.3
# e=0.1
# print(c+d-e+c)         #python是动态语言，精确度不确定，最好不要用浮点数去进行计算
#round(目标数字,精确的位数)
# print(round(c+d-e+c,1))
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a//b)

#判断奇偶数的时候，会用到模运算%，x%2==0就是偶数

#赋值运算符 ： = += -=
# x=3
# # print(x)
# x+=2     #等同于x=x+2
# print(x)

#比较运算符 ==  !=  >  >=  <   <=
#运算结果是布尔值  True  False
# x=5
# y=2
# print(x>=y)

#字符串的字母是区分大小写的
# x='get'
# y='GET'
# print(x==y)


#逻辑运算符  and  or  not   优先级not>and>or
#and  两边为真才为真   真真为真    一假则假
#or   只要有一边为真就为真   假假为假  一真则真
#运算结果是布尔值  True  False
# a=5
# b=0
# print(a and b)


#成员运算符  in、not in   字符串  元组   列表  字典    可迭代数据类型
#运算结果是布尔值  True  False
# s='python'
# print('p' in s)

# s=('python',9,0.33)  #python是元组里的一个元素
# print('p' in s)      #s指的是元组整体，python是个整体，所以这个是False
# print('p'in s[0])    #s[0]指的是python中的p，这个是True

# d={"age":20,"name":"七月"}
# print(20 in d.values())
# print(d.values())
# print(d.keys())

a=5
b=10
#非空非零数据 True   #空 0 False
print(a and b)        #print(a and b)----->10