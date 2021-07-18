# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> list_test
# @Description   : **
# @Time          : 2021/7/13 16:00 
# @Author        : ly
myList = [132, 'asd', 5.362]
print(myList)
print(myList[:-1])
myList += [789, 'quioe']
print(myList)
myList.append("append")
print(myList)
myList.insert(5, 'ewrw')
print(myList)
myList.remove(132)
del myList[3:]
print(myList)
# 遍历取
nestList = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
clo = [i[1] for i in nestList]
print(clo)
