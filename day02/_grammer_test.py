# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> _grammer_test.py
# @Description   : **
# @Time          : 2021/7/18 10:25 
# @Author        : ly
# 1.if语句
if 1 > 2:
    print('true')
else:
    print("false")
# 2.三元表达式
print('ceshi' if 1 < 2 else 'hehe')
# 3.一行写几条语句，也是python唯一用分号的地方

# 4.while语句
#  while else
x = 20
while x < 20:
    print(x)
    x += 1
else:
    print('x>20')
# 5.for
sum0 = 0
for i in [1, 2, 3, 4, 5]:
    sum0 += i
print(sum0)
# for嵌套
sumI = sumJ = 0
for i in range(0, 5, 1):
    sumI += i
    for j in range(5):
        sumJ += sumI + j
print('sumI=' + str(sumI) + '  ' + 'sumj=' + str(sumJ))
# 6.并行遍历：zip和map
# zip合并列表元素生成元组列表
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = [9, 10, 11, 12]
tupleList = zip(l1, l2, l3)
print(tupleList)
for (x, y, z) in tupleList:
    print(str(x) + "   " + str(y) + "   " + str(z))
# zip构建字段
keysList = ["id", "name", "department"]
valsList = ["001", "jeffrey", "sales"]
zipdict = dict(zip(keysList, valsList))
print(zipdict)

# map 根据提供的函数对指定序列做映射
myMap = map(lambda xx: pow(xx, 3), [1, 2, 3, 4, 5])  # 使用 lambda 匿名函数
myList = []
for x in myMap:
    myList.append(x)
print(myList, end="")
# enumerate 得到元素和索引下标

# 文件内容循环读取
# 打开流
# fr = open("d:/123.txt")
# # 条件判断
# while True:
#     # 读取
#     char = fr.read(1)
#     if not char:
#         break
#     print(char, end="")
# # 关闭流
# fr.close()

# file = open("d:/123.txt")
# for char in file.read():
#     print(char, end="")
# file.close()

# file = open("d:/123.txt")
# # 最快读取方式
# for line in file.readlines():
#     print(line.strip())
# file.close()
