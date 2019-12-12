# -*- coding: utf-8 -*-
# @Time:2019/10/30 0030 22:42
# @Author:cp
# @Email:1171954100@qq.com
# @File:homework_0221.py

#完成1-10的整数数字相加，并将结果打印
#while循环
# sum=0
# a=1
# while a<=10:
#     sum+=a
#     a+=1
# print("1-10整数数字相加的结果为:",sum)

#for循环
# n=[1,10,20,40,50,60,70,80,90,100]
# sum=0
# for i in n:
#     print(i)
#     sum=sum+i
# print("整数数字相加的结果为:",sum)

# n=[1,2,3,4,5,6,7,8,9,10]
# sum=0
# for i in n:
#     print(i)
#     sum=sum+i
# print("1-10整数数字相加的结果为:",sum)

# sum=0
# for i in range(1,11):         #for(i=1;i<11;i++)
#     sum=sum+i
# print("1-10整数数字相加的结果为:",sum)


#三角形
'''
    *
   ***
  *****
 *******
*********
'''
# for i in range(1,6):
#     print(" "*(5-i)+"*"*(2*i-1))

'''
*
**
***
****
*****
'''
# for i in range(1,6):
#     print("*"*i)

# class Rectangle():
#
#     def rectangle(self,line):
#         for i in range(1,line+1):
#             print(' '*(line-i)+'*'*(2*i-1))
#
# if __name__ == '__main__':
#     obj=Rectangle()
#     obj.rectangle(5)


# class Rectangle():
#
#     def rectangle(self,line):
#         for i in range(1,line+1):
#             print(' '*(i-1)+'*'*(2*line-(2*i-1)))
#
# if __name__ == '__main__':
#     obj=Rectangle()
#     obj.rectangle(5)

'''
*****
****
***
**
*
'''
# for i in range(1,6):
#     print('*'*(5-(i-1)))

'''
*********
 *******
  *****
   ***
    *
'''
# for i in range(1,6):
#     print(" "*(i-1)+"*"*(2*5-(2*i-1)))


'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
# for i in range(1,6):
#     print(" " *(5-i)+" *"*i)

# #冒泡算法
# s=[6,99,101,34,78,2]#最小的数字在前面  最大的数字在后面
# #两两比较  n-1次
# #第一轮:6 99 34 78 2 101
# #第二轮:6 34 78  2 99 101
# #第三轮:6 34 2  78 99 101
# #第四轮:6 2  34 78 99 101
# #第五轮:2 6 34 78  99 101
# s.sort()
# print(s)

#有1,2,3,4 这四个数字，能组成多少个互不相同且无重复的三位数？分别是什么？
#a b c   a!=b b!=c a!=c
# count=0
# L=[]
# for a in  range(1,5):
#     for b in range(1,5):
#         for c in range(1,5):
#             if a!=b and b!=c and a!=c:
#                 count+=1
#                 L.append(a*100+b*10+c)
#                 # print('符合条件的值是', a * 100 + b * 10 + c)
# print(count)
# print('符合条件的值是',L)


#经典冒泡算法：利用for循环，完成a=[1,7,4,89,34,27]
#冒泡排序，小的排在前面，大的排在后面
#相邻两个数进行比较
# a=[1,7,4,89,34,2]
# print(len(a))
# #1：[1,4,7,34,2,89]
# #2：[1,4,7,2,34,89]
# #3：[1.4,2,7,34,89]
# #4：[1,2,4,7,34,89]
# #冒泡排序至多n-1次
# for j in range(len(a)-1):      #控制循环次数 n-1次循环
#     '''下面这个for循环的作用是完成每一次相邻两个数据的比较，并且完成数值的交换'''
#     for i in range(len(a)-1):  #0 1 2 3 4 5  索引
#         if a[i]>a[i+1]:
#             a[i],a[i+1]=a[i+1],a[i]         #值进行相互互换
# print(a)

#1.根据你输入的数据，来进行判断学生成绩，输入数据函数input()
# score=int(input("请输入你的成绩进行判断"))
# if score > 90:
#     print("成绩优秀!")
# elif score>70:
#     print("成绩良好！")
# elif score>60:
#     print("成绩及格")
# else:
#     print("成绩不及格")

#2.一家商场在降价促销，如果购买金额50-100元之间，包含50元和100元，会给10%折扣，
#如果购买金额大于100元会给20%折扣。编写一程序，询问购买价格，在显示出折扣（10%或20%）和最终价格
# price=int(input("请输入金额"))
# if 50<=price<=100:
#     print("你享受的价格是10%，需要支付的金额是{}".format(0.9*price))
# elif price>100:
#     print("你享受的价格是20%，需要支付的金额是{}".format(0.8 * price))
# else:
#     print("不享受折扣，需要支付原价{}".format(price))

#3.请输入一个数，判断一个数n能同时被3和5整除
# number=int(input("请输入数字"))
# if number%3==0 and number%5==0:
#     print("{}同时被3和5整除的数字".format(number))
# else:
#     print("{}不能同时被3和5整除".format(number))

#4.输入一个5位数，判断它是不是回文数
#即12321是回文数，个位与万位相同，十位与千位相同，根据判断打印出响应信息
#注意：01210是4位数
# number=input("请输入数字")
# if number.isdigit():
#     if len(number)==5:
#         if number[0]!='0':         #为什么要加引号？因为number是字符串类型
#             if number[0]==number[4]  and number[1]==number[3]:
#                 print("{}是回文数".format(number))
#             else:
#                 print("{}不是回文数".format(number))
#         else:
#             print("数据输入有误，请重新输入一个5位数")
#     else:
#         print("请输入5位纯数字")
# else:
#     print("请输入纯数字")
# print(type(number))

#5.利用random函数生成随机整数，从1到9取出来，然后输入一个数字，来猜，如果大于，则打印bigger，小了就打印less
#如果相等，则打印equal
# import random
# number=random.randint(1,9)
# guess=int(input("请输入一个数字"))
# if guess>number:
#     print("bigger")
# elif guess<number:
#     print("less")
# else:
#     print("equal")

#拓展题:
#登录功能：用户名和密码存在{'name':'huahua','pwd':'123456'}字典中
#通过控制台输入用户名和密码判断是否正确，然后给出相应的提示信息：登录成功 or 用户名或密码错误
# user_info={'name':'huahua','pwd':'123456'}
# username=input("请输入用户名：")
# if username==user_info['name']:
#     pwd=input("请输入密码：")
#     if pwd==user_info['pwd']:
#         print("登录成功")
#     else:
#         print("密码不正确")
# else:
#     print("用户名不正确")

#人机大战
# #1：人和机器进行猜拳游戏写一段程序，首先选择角色：1 曹操 2张飞 3 刘备，然后选择的角色进行猜拳：1剪刀 2石头 3布 玩家输入一个1-3的数字
# #；然后电脑出拳 随机产生1个1-3的数字，提示电脑出拳结果（ 1剪刀 2石头 3布 ） ，双方出拳完毕后：角色和机器出拳对战，对战结束后，最后出示
# #本局对战结果...赢...输,然后提示用户是否继续？按y继续，按n退出。最后结束的时候输出结果 角色赢几局 电脑赢几局，平局几次 游戏结束

import random
pc_win=0
human_win=0
ping=0
role_dict={'1':'曹操','2':'张飞','3':'刘备'}
fist_dict={'1':'剪刀','2':'石头','3':'布'}

#选择角色
while True:
    role_num=input('请输入选择的角色：1 曹操 2张飞 3 刘备')
    if role_num in ['1','2','3']:
        role_name=role_dict[role_num]   #d[key]
        print(role_name)
        break
    else:
        print('角色选择有误，请重新输入1,2,3 ')
        continue

while True:
    #角色出拳
    while True:
        human_fist_num=input('请出拳：1 剪刀 2石头 3 布')
        if human_fist_num in ['1','2','3']:
            human_fist_value=fist_dict[human_fist_num]         #d[key]
            print('{}出拳为：{}'.format(role_name,human_fist_value))
            break
        else:
            print('出拳错误 ')
            continue

    #电脑出拳
    pc_fist_num=random.randint(1,3)    #这里产生的是整数，1,2,3
    print('pc出拳为:{}'.format(fist_dict[str(pc_fist_num)]))    #转成字符串

    #对战
    #human win
    #human  1----pc  3--->  -2
    #human  2----pc  1--->  1
    #human  3----pc  2--->  1

    #pc  win
    #human  1----pc  2--->  -1
    #huamn  2----pc  3--->  -1
    #human  3----pc  1--->  2

    if int(human_fist_num)-pc_fist_num in [-2,1]:
        print("{}win".format(role_name))
        human_win+=1
    elif int(human_fist_num)-pc_fist_num in [-1,2]:
        print("pc win")
        pc_win+=1
    else:
        print("双方平局")
        ping+=1

    #是否继续
    choice=input("是否继续？n退出,任意键继续")
    if choice=='n':
        break
    else:
        continue

#输出结果
print("{}赢了{}局，pc赢了{}局，平了{}局".format(role_name,human_win,pc_win,ping))