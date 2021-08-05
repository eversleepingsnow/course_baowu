# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> _xarray_test.py
# @Description   : **
# @Time          : 2021/8/5 12:32 
# @Author        : ly
import numpy as np
import pandas as pd
import xarray as xr

# 创建DataArray
data = np.random.randn(4, 3)
times = pd.date_range('20210805', periods=4)
loc = ['Beijing', 'Shanghai', 'Xi\'an']
foo = xr.DataArray(data, coords=[times, loc], dims=['time', 'city'])
print(foo)

# 创建  不设坐标
foo1 = xr.DataArray(data)
print(foo1)

# 创建元祖序列作为坐标
data = np.random.randn(4, 3)
times = [('2021-08-05'), ('2021-08-06'), ('2021-08-07'), ('2021-08-08')]
loc = [('Beijing'), ('Shanghai'), ('Xi\'an')]
foo2 = xr.DataArray(data, coords=[('time', times), ('city', loc)])
print(foo2)
