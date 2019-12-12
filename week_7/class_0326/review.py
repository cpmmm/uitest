# -*- coding: utf-8 -*-
'''
@time: 2019/11/16 0016 22:35
@author: chen
@contact: 1171954100@qq.com
@file: review.py
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
'''ddt框架第二节课，主要是讲面试题。
作业讲解在homework_0323里'''




'''
数据类型
1.string
2.int
3.float
4.boolean  条件判断或者逻辑控制的依据，多种运算形式的返回值
    if 1 >  2或者  while True 或 while 1
    
5.list  有顺序的容器，可变的
6.dict  没有顺序的，可变的
#为什么说字典是无序的？
my_dict={"name":'chen','age':"18","sex":"男"}
for key,value in my_dict.items():
    print(key,value)
    
7.tuple  用来解包  ，不可变类型
如果只有一个元素，需要是这个样子,需要加一个逗号  (1,)



逻辑控制，流程控制，控制流程
条件  if...elif...else
遍历  for...in...
while
continue  break


函数
1.参数：形式参数，实际参数，位置参数，关键字参数，默认参数，动态参数
2.return  遇到return  终止运行
          没有return  返回None
'''
#面试题
#1.range()的特性，是一种跟列表非常相似的数据结构
# print(type(range(1,2)))


#2.字符串不能修改里面的内容，因为字符串是不可变类型
# str1='myclass'
# str1[2]='s'
# print(str1)


#3.务必搞懂，经典面试题  80%几率被考到
#3.1  可变参数作为函数的默认值
# def add(a,mylist=[]):
#     mylist.append(a)
#     return mylist
#
# print(add.__defaults__)   #这个可以用来观察
# print(add(4))          #[4]
# print(add.__defaults__)
# print(add(5))          #[4,5]   添加完4之后，默认mylist里是mylist[4]，已经有个4了，所以是[4,5]
# print(add.__defaults__)
# print(add(6,['a']))    #['a',6]   [a]是实际参数，所以直接替换了mylist[4,5],然后给a传参是6，从后面追加，所以是['a',6]
# print(add.__defaults__)
# print(add(7))          #[4,5,7]  这个是因为默认参数是[4,5]，直接给a传参是7，所以是[4,5,7]
# print(add.__defaults__)


#3.2  上面那个提出改进计划
#最简单方法,每次都传一个实际参数进去
# print(4,[])
# print(5,[])
# print(6,[])

#第二种解决方法
# def add(a,mylist=[]):
#     if not mylist:      #not后面是布尔值，字符串空，整数是否为0，list是否为空，None，dict是否为空
#         new_list=[]
#         new_list.append(a)
#         return new_list
#     mylist.append(a)
#     return mylist

# print(add.__defaults__)   #这个可以用来观察
# print(add(4))
# print(add.__defaults__)
# print(add(5))
# print(add.__defaults__)
# print(add(6,['a']))
# print(add.__defaults__)
# print(add(7))
# print(add.__defaults__)

#第三种解决方案,默认值设为不可变类型
# def add(a,mylist=None):
#     if not mylist:      #not后面是布尔值，字符串空，整数是否为0，list是否为空，None，dict是否为空
#         new_list=[]
#         new_list.append(a)
#         return new_list
#     mylist.append(a)
#     return mylist
#
# print(add.__defaults__)   #这个可以用来观察
# print(add(4))
# print(add.__defaults__)
# print(add(5))
# print(add.__defaults__)
# print(add(6,['a']))
# print(add.__defaults__)
# print(add(7))
# print(add.__defaults__)

#4.  __init__和__new__的区别
     #实现一个单例
     #类属性和实例属性

# class Movie:
#     #类属性
#     workers=["导演","制片人","编剧","灯光师"]
#
#     def __init__(self,name):
#         self.workers=[]
#         self.name=name
#
#     # def __new__(cls, *args, **kwargs):        #没注释返回None，是因为没有返回任何东西
#     #     pass
# #movie1=Movie("喜剧之王")
# # print(Movie("喜剧之王"))
# # print(Movie("喜剧之王").workers)   #[]   对象会找对象属性
# # print(Movie.workers)             #["导演","制片人","编剧","灯光师"]  类会找类属性
#
# #这个可以理解为盗版的，和上面的不是同一个对象
# #movie2=Movie("喜剧之王")
# Movie("喜剧之王").workers=['导演']
#
# #movie3=Movie("喜剧之王")
# print(Movie("喜剧之王").workers)           #[]
# print(Movie.workers)                     #["导演","制片人","编剧","灯光师"]

#os.path   路径
#异常处理   try...except Exception  as  e...:

#捕获异常和抛出异常有什么关系
try:
    1/0
    print("没出错!")
except Exception as e:       #捕获异常
    print("出错喽!")
    raise                    #raise抛出异常

#文件处理 打开文件以后，一定要注意关闭

#excel操作

#logging
#parseconfig...  配置文件

#单元测试  unittest
#TestCase，Suite  收集用例的容器 ，loader  添加模块 类    ，addTest  对象
#TextTestRunner,HTMLTestRunner

#DDT  装饰类@ddt.ddt   测试用例@ddt.data(*)     脱衣服@ddt.unpack

#excel
#1.workbook
#2.sheet
#3.cell   对象==>  值  cell.value  =>字符串，要进行转换
