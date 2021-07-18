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
sex = b'female'
job = b'teacher'

bin_buf_all = struct.pack('4si6s7s', name, age, sex, job)
print(bin_buf_all)
fp.write(struct.pack('4si6s7s', name, age, sex, job))
fp.flush()
fp.close()
# 读取
fd = open('E:/code/pyTest/course_baowu/test.txt', 'rb')
offset = struct.calcsize('4si6s7s')
str2 = struct.unpack('4si6s7s', fd.read(offset))
print(str2)
fd.close()

