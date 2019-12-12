# -*- coding: utf-8 -*-
# @Time:2019/10/29 0029 9:29
# @Author:cp
# @Email:1171954100@qq.com
# @File:liebiao.py

#列表 list []
#1.空列表  L=[]
# L=[]
# print(type(L))

#2.列表里面的元素可以是任意类型，不同元素之间用逗号隔开
# L=[1,0.02,'hello',True,(1,2,3,666,'python'),['Python','Java','Ruby']]

#  0   1     2      3            4                     5      正序
# -6  -5     -4     -3           -2                    -1     反序
#3.列表是有索引index，正序/反序编号都支持  取值方式同字符串
    #单个取值  列表名[索引值]  比如取True
# print(L[3])
# print(L[-3])

    #切片     列表名[索引头:索引尾:步长] 步长默认是1
    #嵌套取值  倒序输出Java这个元素
# print(L[-1][1][::-1])

#4.列表是有序可变类型
# L=[1,0.02,'hello',True,(1,2,3,666,'python'),['Python','Java','Ruby']]
# L[2]='xiaoming'
# print(L)

#列表和元组并不是绝对的不能修改
t=(1,0.02,'hello',True,(1,2,3,666,'python'),['Python','Java','Ruby'])
L=[1,0.02,'hello',True,(1,2,3,666,'python'),['Python','Java','Ruby']]

#修改元组中列表里的元素  将元组中的列表里的Rudy改为javascript
t[-1][-1] = 'javascript'
print(t)

#修改列表中的元组       将列表中的元组(1,2,3,666,'python')修改为柠檬班
L[-2]='柠檬班'
print(L)

