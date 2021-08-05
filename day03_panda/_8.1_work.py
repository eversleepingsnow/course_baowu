# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> _8.1_work.py
# @Description   : **
# @Time          : 2021/8/5 12:32
# @Author        : ly
"""
A:06_descriptionStat.py举一反三，用你们自己的数据测算
"""
import pandas as pd
import numpy as np

data = {
    'deltP': pd.Series([203.28, 204.24, 204.39, 204.57, 202.91, 202.93, 198.68, 191.42, 188.09, 185.47]),
    'K': pd.Series([2.82, 2.84, 2.87, 2.87, 2.84, 2.83, 2.76, 2.64, 2.59, 2.57]),
    'sigmaBP': pd.Series([22.69, 24.60, 29.17, 27.27, 26.09, 28.73, 21.42, 40.31, 20.41, 41.44]),
    'expo': pd.Series([59.25, 51.84, 48.75, 51.84, 49.06, 42.58, 49.99, 42.58, 54.31, 44.74])
}
df = pd.DataFrame(data)
print(df)
print('-------------')
print(df.sum())
print('-------------')
print(df.sum(1))
print('-------------')
print(df.mean())
print('-------------')
print(df.std())
print('-------------')
print(df.describe())
print('-------------')
# include用于传递列总结的必要信息的参数
df['test'] = pd.Series(['test1', 'test2', 'test1', 'test2', 'test1', 'test2', 'test1', 'test2', 'test1', 'test2'])
print(df.describe(include=['object']))
print('-------------')
print(df.describe(include='all'))
print('------next-------')
"""
B:07_func.py 举一反三，用你们自己的数据测算
"""


# 管道 声明函数
def adder(val1, val2):
    return val1 + val2


# 创建DataFrame
df = pd.DataFrame(np.random.randn(5, 3), columns=['col1', 'col2', 'col3'])
print(df)
df1 = df.pipe(adder, 100)
print(df1)
print("列均值")
print(df1.apply(np.mean))
print("行均值")
print(df1.apply(np.mean, axis=1))
# 嵌入匿名函数求解
print("列最大值减去最小值")
df2 = df1.apply(lambda x: x.max() - x.min())
print(df2)
print("通过map函数仅对指定列运算")
print(df1['col1'].map(lambda x: x * 2))
print("通过applymap函数对DataFrame所有可计算数据运算")
print(df1.applymap(lambda x: x - 200))

"""
C:08_RebuildIndex.py 用你们自己的数据测算
"""
print('------next-------')
N = 15
df_08 = pd.DataFrame({
    'A': pd.date_range('20200805', periods=N, freq='D'),
    'x': np.linspace(1, stop=N, num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low', 'Mid', 'High'], N).tolist(),
    'D': np.random.normal(50, 5, size=N).tolist()
})
print(df_08)
print('-------------')
# 重建索引
df_reindexed = df_08.reindex(index=[1, 2, 5], columns=['x', 'y'])
print(df_reindexed)

# reindex_like
df1 = pd.DataFrame(np.random.rand(5, 3), columns=['a', 'b', 'c'])
df2 = pd.DataFrame(np.random.rand(3, 3), columns=['a', 'b', 'c'])
print(df1)
print('-------------')
print(df2)
print('-------------')
print(df2.reindex_like(df1))
print('-------------')
'''
reindex()填充
pad/ffill - 向前填充值(向下复制填充最近的非NaN数据)
bfill/backfill - 向后填充值(向上复制填充最近的非NaN数据)
nearest  - 从最近的索引值填充(NaN的数据由最近的非NaN数据复制填充)
'''
print("向前填充")
print(df2.reindex_like(df1, method='ffill', limit=1))
print("向后填充")
print(df2.reindex_like(df1, method='bfill'))

# 重命名行列
print(df1.rename(columns={'a': 'hehe', 'b': 'ahha'}, index={0: 'qwer'}))
