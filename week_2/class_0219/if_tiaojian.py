# -*- coding: utf-8 -*-
# @Time:2019/10/29 0029 15:50
# @Author:cp
# @Email:1171954100@qq.com
# @File:if_tiaojian.py

#1.非常简单的条件语句
#if  条件:    #if后面的条件运算结果是布尔值    逻辑/比较/成员   各类数据类型
    #if代码   只有当if后面的条件成立的时候（为True的时候,1就是True，非空非零数据也是True）才会执行if的代码块

# age=18
# if age==18:
#     print('小明今年是18岁！')
#
# if 1:
#     print('小明今年是18岁！')
#
# if 9:
#     print('小明今年是18岁！')

# s=[]
# if s:
#     print("小明今年是18岁！")     #不执行

#在python中，非空非零数据为True ； 空数据、零为False


#2.  if..else..语句
# age=17
# if age==18:
#     print("小明今年是18岁！")
# else:
#     print("小明今年还没到18岁！")

# age=55
# if age>=18:
#     print("小明是个成年人了")
#     if age>40:
#         print("他是个中年人")
#     else:
#         print("他是一个青少年")
# else:
#     print("他今年还是未成年")

#3.多重判断语句：if...elif...elif...else
#if 必须要有的  else  elif  可有可无  但是else一定是放到最后的
#elif的个数不限定

score=int(input("请输入整数"))       #input是str类型，我刚输入的100是int，所以类型不匹配，需要在input外面加上int
if score>=90:
    print("great!!!")
elif score>80:
    print("good!!!")
elif score>70:
    print("well!!!")
elif score>=60:
    print("pass")
else:
    print("no pass")
