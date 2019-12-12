# -*- coding: utf-8 -*-
# @Time:2019/11/2 0002 17:23
# @Author:cp
# @Email:1171954100@qq.com
# @File:file_wenjian_lujing.py

#文件的新建  读取  写入数据
#open()#新建文件的操作
#r 只读  如果我们要进行读或者写的文件里面有中文  那么就要设置编码为utf-8
# file=open('python15.txt','r+',encoding='utf-8')#获取文件的操作权限  然后进行读或者写操作    有返回值用一个变量file接收
# res=file.read(10)     #读取的字符的长度，也可以不写长度
# print(res)
# file.write("double")
# print(file.tell())
# file.seek(0,0)
# file.close()
#r只读，读取的文件必须要存在，否则就会报错
#r+读写,可以进行读写操作，但是目标文件必须要存在，否则就会报错，写入的内容就会写在后面
#写在指定位置  tell()获取当前位置    seek(offset,where)偏移光标/位置--了解
#offset  0  3   6   9 随便写
#where  0头部  1当前位置   2尾部

# w只写  清空写  如果文件存在就清空写   如果文件不存在，就会新建文件再去写
# file=open('python15.txt','w',encoding='utf-8')
# # file.read()  不可读，只能写
# file.write("你看这个碗它又大又圆！")
# file.close()
#w+读写
#同上

# a追加   如果文件存在，直接追加；如果文件不存在，就会新建文件再去写
# file=open('python16.txt','a',encoding='utf-8')
# file.write("窗外的麻雀")
# file.close()

# a+读追加  如果文件存在，直接追加；如果文件不存在，就会新建文件再去写,可以读
# file=open('python16.txt','a+',encoding='utf-8')
# file.seek(0,0)   #因为追加是在最后面追加，所以光标在最后面，但是通过偏移，光标在最前面就可以读出内容了
# print(file.read())
# file.write("窗外的麻雀")
# file.close()

# rb，rb+，wb，wb+，ab，ab+  文件流的形式的去写入文件的时候 binary
