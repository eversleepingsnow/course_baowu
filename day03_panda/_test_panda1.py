# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> _test_panda1.py
# @Description   : **
# @Time          : 2021/7/25 17:00 
# @Author        : ly
import pandas as pd
import numpy as np

print(pd.__version__)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

# 通过值传递来创建一个系列
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# 通过传递numpy数组，使用datetime索引和标记列来创建DataFrame
dates = pd.date_range('20210725', periods=7)
print(dates)
df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
print("**************************")

# 使用标签获取截面
print(df.loc[dates[3]])

# 使用字典创建DataFrame
dic = {
    'A': 1.,
    'B': pd.Timestamp('20210805'),
    'C': pd.Series(1, index=list(range(1, 5, 1)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(['test', 'train', 'test', 'train']),
    'F': 'foo'
}
df2 = pd.DataFrame(dic)
print(df2)

# 显示前三条
print(df2.head(3))
# 显示后三条
print(df2.tail(3))

print("显示列和底层numpy数据")
print(df2.index)
print(df2.columns)
print(df2.values)

print("显示数据的快速统计摘要")
print(df.describe())
print(df2.describe())

print("轴排序 -- 列倒序")
print(df.sort_index(axis=1, ascending=False))
print(df.sort_index(ascending=False))
print(df.sort_values(by="C", ascending=False))
"""
    选择区块
"""
print("---------------df---------------")
print(df)
print(df['B'])
print(df[2:5])
"""
# 选择指定索引列
# 使用标签获取横截面
# 使用标签选择多轴
# 标签索引、列切片
# 获取标量值
# 通过传递的整数获取位置
"""

# 选择指定索引列
print(df['20210726':"20210728"])
# 通过传递的整数获取位置
print(df.iloc[3])