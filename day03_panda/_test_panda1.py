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

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# 通过传递numpy数组，使用datetime索引和标记列来创建DataFrame
dates = pd.date_range('20210725', periods=7)
print(dates)
df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
print(df.loc[dates[3]])
