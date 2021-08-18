# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> _pandas_test_date.py
# @Description   : **
# @Time          : 2021/8/6 10:23 
# @Author        : ly
import pandas as pd
import datetime

# 创建日期范围
datelist = pd.date_range(start='20210806', end='20210831')
print(datelist)
print('----------------------------------------------------')
# 更改日期频率 主要修改freq的参数值
# 构造时间
start = datetime.datetime(2021, 8, 6)
end = datetime.datetime(2021, 8, 10)
dates = pd.bdate_range(start,end)
print(dates)
