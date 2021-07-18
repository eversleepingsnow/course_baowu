# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> day01_work.py
# @Description   : **
# @Time          : 2021/7/12 20:27 
# @Author        : ly
from datetime import datetime
import pickle

'''
2.定义元祖对象tuple包含数据1,2,3,4,5
将元祖对象保存在c:/tuple.txt中
定义新的元祖对象tuple1从c:/tuple.txt获取之前保存的元祖对象并打印结果
'''
test_tuple = (1, 2, 3, 4, 5)
myfile = open("d:/tuple.txt", "wb")
pickle.dump(test_tuple, myfile)
myfile.close()

myfile1 = open("d:/tuple.txt", "rb")
test_tuple1 = pickle.load(myfile1)
myfile1.close()
print(test_tuple1)

'''
1.定义字典对象结构如下:
字典person定义奥黛丽赫本的信息
name节点包括
  firstName=Audrey
  lastName=Hepburn
three_dimensional节点包括
  chest=88
  waist=20
  hip=89
birthday=1929-05-04(必须是python的日期格式)
定义完成后调用person可以打印出完整的person字典结构
调用person的three_dimensional中的waist得到结果20
'''
person = {}
birthday = datetime.strptime("1929-05-04", "%Y-%m-%d").date()
person = {"name": {"firstName": "Audrey", "lastName": "Hepburn"},
          "three_dimensional": {"chest": "88", "waist": "20", "hip": "89"},
          "birthday": birthday
          }
print(person)
print(person["three_dimensional"]["waist"])
