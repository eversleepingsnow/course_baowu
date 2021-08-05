# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> _test_pandas2.py
# @Description   : **
# @Time          : 2021/8/5 14:07 
# @Author        : ly
import pandas as pd
import numpy as np

N = 10
df = pd.DataFrame({
    'A': pd.date_range(start='2021-08-05', periods=N, freq='D'),
    'x': np.linspace(1, stop=N, num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low', 'Mid', 'High'], N).tolist(),
    'D': np.random.normal(100, 10, size=N).tolist()
})
print(df)
# 遍历列名
for col in df: print(col)
print('---------------------')
# iteritems()
for key, value in df.iteritems():
    print(key, value)
print('---------------------')
# iterrows()返回迭代器，产生每个索引值以及包含每行数据的序列
for row_index, value in df.iterrows():
    print(row_index, value)
for row in df.itertuples():
    print(row)