# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> struct_test.py
# @Description   : **
# @Time          : 2021/7/18 9:38 
# @Author        : ly
import struct

# 写入
fp = open('E:/code/pyTest/course_baowu/test.txt', 'wb')
name = b'plly'
age = 15
sex = b'famel'
job = b'teacher'
fp.write(struct.pack('4si5s7s'), name, age, sex, job)
fp.flush()
fp.close()
# 读取
fd = open('E:/code/pyTest/course_baowu/test.txt', 'r')
