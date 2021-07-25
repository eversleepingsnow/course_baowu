# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> _numpy_test02.py
# @Description   : **
# @Time          : 2021/7/25 9:39 
# @Author        : ly
import numpy as np

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
a = np.arange(9).reshape(3, 3)
for element in a.flat:
    print(element, end=",")

a = np.arange(8).reshape(2, 2, 2)
print('\n' + '原数组：')
print(a)
print('获取数组中一个值：')
print(np.where(a == 6))
print(a[1, 1, 0])  # 为 6
print('\n')
# 向后滚动指定的轴
b = np.rollaxis(a, 1, 0)
print(b)
c = np.rollaxis(a, 2, 1)
print(c)

# 创建了三维的 ndarray
a = np.arange(8).reshape(2, 2, 2)

print('原数组：')
print(a)
print('\n')
# 现在交换轴 0（深度方向）到轴 2（宽度方向）

print('调用 swapaxes 函数后的数组：')
print(np.swapaxes(a, 2, 0))
print(np.swapaxes(a, 0, 2))

x = np.array([[1], [2], [3]])
y = np.array([4, 5, 6])

# 对 y 广播 x
b = np.broadcast(x, y)
# 它拥有 iterator 属性，基于自身组件的迭代器元组

print('对 y 广播 x：')
r, c = b.iters

# Python3.x 为 next(context) ，Python2.x 为 context.next()
print(next(r), next(c))
print(next(r), next(c))
print(next(r), next(c))
print(next(r), next(c))
print(next(r), next(c))
print(next(r), next(c))
print(next(r), next(c))
print(next(r), next(c))
print(next(r), next(c))

'''
numpy.expand_dims 函数通过在指定位置插入新的轴来扩展数组形状
numpy.expand_dims(arr, axis)
axis：新轴插入的位置
'''
x = np.array(([1, 2],
             [3, 4]))
print(x)
print(x.shape)
y = np.expand_dims(x, axis=0)
print(y)
print(y.shape)
y = np.expand_dims(x, axis=1)
print(y)
print(y.shape)
