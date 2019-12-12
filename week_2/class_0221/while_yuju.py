# -*- coding: utf-8 -*-
# @Time:2019/10/30 0030 11:18
# @Author:cp
# @Email:1171954100@qq.com
# @File:while_yuju.py


#while循环&for循环&嵌套循环
#函数语句&内置函数

#什么时候才会用到循环：重复的操作

#while循环
#语法  while  条件表达式:     #条件表达式-->本质：布尔值  逻辑  比较  成员  各种数据类型
        #循环体

#死循环
#有一个风险：容易进入死循环
# while 1:
#     print('python是世界上最优美的语言')

#1）while后面不要是永真式，那么while后面的表达式的值 是要变化的
# a=0
# while a<5:
#     a+=1
#     print('python是世界上最优美的语言')

#2）while后面是永真式，那么可以用break continue组合的方法来防止进入死循环
#break 终止循环
#continue  结束本轮循环  继续下一轮循环
# while 1:
#     print('python是世界上最优美的语言')
#     break

# a=0
# while 1:
#     a += 1
#     if a<3:  # 1   2
#         print('python是世界上最优美的语言')
#         continue
#     else:
#         break

#练习：有一个空列表s=[]  我们利用while循环  循环5次  每次询问一个人的名字
#并且把名字加到列表里面去
#温馨提示  列表增加元素  就可以用这个方法  列表名.append(值)
#1）
# s=[]
# a=0
# while 1:
#     if a<5:
#         name=input("请输入姓名")
#         s.append(name)
#         a+=1
#         continue
#     else:
#         break
# print(s)

#2）
# s=[]
# a=0
# while a<5:
#     name=input("请输入姓名")
#     s.append(name)
#     a+=1
# print(s)

#3）
s=[]
while len(s)<5:
    name = input("请输入姓名")
    s.append(name)
print(s)



