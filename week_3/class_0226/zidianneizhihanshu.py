# -*- coding: utf-8 -*-
# @Time:2019/11/1 0001 10:57
# @Author:cp
# @Email:1171954100@qq.com
# @File:zidianneizhihanshu.py

# d={'name':'lemon','age':22,'score':'99.99'}
# #增加和改
# #key  要求数据类型是不可变的，唯一不重复  字典名[key]
# #字典名[key]=value  如果key是已经存在的，那就是修改。如果key是不存在的，就是新增
# print(d['name'])
# d['name']='summer'   #key是唯一的，有多个就可以覆盖
# d['sex']='男'
# print(d)

#查  取值  字典名[key]

#删除  pop()
d={'name':'lemon','age':22,'score':'99.99'}
# d.pop('name')      #因为是字典是无序的，所以需要给它指定key
# d.popitem()        #随机删除，不需要指定key
# d.clear()          #清空，变成空字典
#print(d)

# res=d.copy()       #复制，有返回值
# res=d.items()      #返回键值对，元组括起来的
# res=d.keys()       #返回key
# res=d.values()     #返回值

res=d.get('age')   #根据key取值 get里面传递的参数是key  跟字典名[key]差不多
print(res)

