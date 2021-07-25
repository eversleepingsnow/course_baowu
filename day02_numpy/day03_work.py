# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> day03_work.py
# @Description   : **
# @Time          : 2021/7/25 16:08 
# @Author        : ly
import numpy as np
import pandas as pd
import xarray as xr
from matplotlib import pyplot as plt
import matplotlib

"""
1.使用arange函数生成一个1到9数字的3 X 3数组a1和一个1到3数字的一维数组a2，通过numpy的broadcast生成数组c2,c2的数组打印结果如下:
[[ 2  4  6]
 [ 5  7  9]
 [ 8 10 12]]

"""
a1 = np.arange(1, 10).reshape(3, 3)
a2 = np.arange(1, 4)
b = np.broadcast(a2, a1)
c, v = b.iters
c2 = np.empty(b.shape)
c2.flat = [c + v for c, v in b]
print(c2)
"""
2.生成1至25数字的5 X 5矩阵a1和1至20的5 X 4矩阵b，通过numpy的数组修改功能生成数组c,c数组打印结果如下:
[[ 1  2  3  4  5  1  2  3  4]
 [ 6  7  8  9 10  5  6  7  8]
 [11 12 13 14 15  9 10 11 12]
 [16 17 18 19 20 13 14 15 16]
 [21 22 23 24 25 17 18 19 20]]
"""
a1 = np.arange(1, 26).reshape(5, 5)
b = np.arange(1, 21).reshape(5, 4)
c = np.concatenate((a1, b), axis=1)
print(c)
"""
3.由3至19数字组成的数组作为x变量，通过公式y=3*x+11，画出点线图：
"""
x = np.linspace(3, 19, 17, dtype=int)
# print(x)
y = 3 * x + 11
plt.title('Matplotlib Demo')
plt.xlabel('x axis caption')
plt.ylabel('y axis caption')
plt.plot(x, y, "-.b")
plt.show()
"""
4.请打印出以下pandas的序列结果：
20    aa
30    bb
40    cc
50    dd
dtype: object
"""
datas = ['aa', 'bb', 'cc', 'dd']
df = pd.Series(datas, index=[20, 30, 40, 50])
print(df)
"""
5.请用字典结构生成以下pandas的DataFrame数据结构，打印效果如下:
         one     two
index1  10.0   40
index2  20.0   50
index3  30.0   60
index4   NaN   70
"""
datas = {
    'one': pd.Series((10., 20., 30.), index=['index1', 'index2', 'index3']),
    'two': pd.Series((40, 50, 60, 70), index=['index1', 'index2', 'index3', 'index4'])
}
df = pd.DataFrame(datas)
print(df)
