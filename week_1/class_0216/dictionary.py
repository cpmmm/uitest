# -*- coding: utf-8 -*-
# @Time:2019/10/29 0029 9:54
# @Author:cp
# @Email:1171954100@qq.com
# @File:dictionary.py

#dictionary  字典{}  dict
#1.空字典
# d={}
# print(type(d))

#2.字典   key:value   键值对 不同的键值对中间用逗号隔开
#key:不可变数据       int  float  boolean  str  tuple
#value:可以是任意类型  int  float  boolean  str  tuple  list  dict
#控制台每次输出的数据都是变化的
#因为True就是1，所以d字典中的我会被后面的罗覆盖掉，而后面的i字典中的我就不会被罗覆盖掉
#是value的覆盖，不是key的覆盖
#key是唯一的  不能重复的  对于python来说  1就是True  0就是False
#key  一般都是用字符串 ''  ""
# d={1:'我',
#    0.02:'爱',
#    True:'罗',
#    'age':22,
#    (1,2,3):tuple}
#
# i={1:'我',
#    0.02:'爱',
#    False:'罗',
#    'age':22,
#    (1,2,3):tuple}
# print(d)
# print(i)

d={"name":"柠檬班",
   "class_name":"python_15",
   "score":[99,98,97],
   "height":{'sadness':170.33,'小明':180.22}}
# print(d)

#3.字典取值：字典名[key]
# print(d["score"])

#4.嵌套取值，确定数据类型，然后取值    例如取sadness的身高      取分数中的99
# print(d["height"]['sadness'])  #字典取值
# print(d["score"][0])           #字典取值，然后在列表取值

#5.字典是可变无序数据类型
d["class_name"] = "柠檬班python15期"   #重新赋值
print(d)