# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> _numpy_io.py
# @Description   : **
# @Time          : 2021/7/25 16:45 
# @Author        : ly
import numpy as np

a = np.array([1, 2, 3, 4, 5])
np.save('test', a)
print(np.load('test.npy'))
