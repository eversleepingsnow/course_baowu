# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> _numpy_test.py
# @Description   : **
# @Time          : 2021/7/18 13:35 
# @Author        : ly

import numpy as np

a = np.array([1, 2, 3])
print(a)
print('_____________________________________')
b = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
print(b)
print('_____________________________________')

dt = np.dtype(np.int32)
print(dt)
print('_____________________________________')
x = (1, 2, 3)
a = np.asarray(x)
print(a)
print('_____________________________________')
x = [(1, 2, 3), (4, 5)]
b = np.asarray(x, dtype='object')
print(b)
print('_____________________________________')
# NumPy 从数值范围创建数组
a = np.arange(5)
print(a)
# 设置dtype 设置了起始值、终止值及步长
a = np.arange(5, 10, 2, dtype=float)
print(a)

# numpy.linspace 函数用于创建一个一维数组，数组是一个等差数列构成的
a = np.linspace(1, 10, 5, )
print(a)
# NumPy 切片和索引
a = np.arange(10)
s = slice(2, 7, 2)
print(a[s])
b = a[2: 7: 2]
print(b)
print(a)
print(a[:5])
a = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a[..., 0])
print(a[..., 1:])
print(a[1, ...])
print('_____________________________________')
# NumPy 高级索引
x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]
print(y)
print('____________花式索引_______________')
# 花式索引
"""
花式索引指的是利用整数数组进行索引。
花式索引根据索引数组的值作为目标数组的某个轴的下标来取值。
对于使用一维整型数组作为索引，如果目标是一维数组，
那么索引的结果就是对应下标的行，如果目标是二维数组，
那么就是对应位置的元素。
花式索引跟切片不一样，它总是将数据复制到新数组中。
"""
x = np.arange(32).reshape(8, 4)
print(x)
print(x[[4, 1, 0, 3]])
# 传入多个索引数组（要使用np.ix_）
print(x[np.ix_([4, 1, 7, 3], [2, 0, 1, 3])])
"""
NumPy 广播(Broadcast)
广播(Broadcast)是 numpy 对不同形状(shape)的数组进行数值计算的方式， 
对数组的算术运算通常在相应的元素上进行。
如果两个数组 a 和 b 形状相同，即满足 a.shape == b.shape，
那么 a*b 的结果就是 a 与 b 数组对应位相乘。这要求维数相同，且各维度的长度相同。
"""
a = np.array([[0, 0, 0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])
b = np.array([1, 2, 3])
print(a + b)
print('_____________________________________')
b = np.array([1])
bb = np.tile(b, (4, 3))
print(a + bb)
"""
NumPy 迭代数组
NumPy 迭代器对象 numpy.nditer 提供了一种灵活访问一个或者多个数组元素的方式。
迭代器最基本的任务的可以完成对数组元素的访问。
"""
a = np.arange(6).reshape(2, 3)
print('原始数组是：')
print(a)
print('\n')
print('___________迭代数组_________________')
print('迭代输出元素：')
for x in np.nditer(a):
    print(x, end=",")
print('\n')
for x in np.nditer(a.T):
    print(x, end=",")
print('\n')
# 控制遍历顺序
for x in np.nditer(a, order='F'):
    print(x, end=",")
print('\n')
for x in np.nditer(a, order='C'):
    print(x, end=",")
print('\n')
for x in np.nditer(a, order='C', op_flags=['readwrite']):
    x[...] = 2 * x
    print(x, end=",")
print('___________*****_________________')
"""
Numpy 数组操作
Numpy 中包含了一些函数用于处理数组，大概可分为以下几类：
    修改数组形状 numpy.reshape 
    numpy.ndarray.flat  返回数组元素迭代器
    numpy.ndarray.flatten   返回一份数组拷贝
    numpy.ravel   展平的数组元素
    翻转数组   
    修改数组维度  numpy.transpose(arr, axes)
    连接数组
    分割数组
    数组元素的添加与删除
"""
a = np.arange(8).reshape(2, 2, 2)

print('原数组：')
print(a)
print('获取数组中一个值：')
print(np.where(a == 6))
print(a[1, 1, 0])  # 为 6
print('\n')