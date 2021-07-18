# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> day02_work.py
# @Description   : **
# @Time          : 2021/7/18 17:20 
# @Author        : ly
"""
1.用while循环语法计算1+2+....+100的基数结果和偶数结果
"""
i = 1
sum_odd = 0
sum_even = 0
while i < 101:
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
    i += 1
else:
    print("循环结束")
print('sum_odd=' + str(sum_odd) + " " + 'sum_even=' + str(sum_even))
"""
2.定义函数catchError(),该函数方法打印指定序列mlist的值，
mlist序列包括值: jack,18,178三个值，
在catchError()函数中试图获取mlist的第4个值，
由于边界越界抛出打印'序列边界越界'字样，其他错误全部不报错，
退出函数时无论序列是否边界越界，都会打印"捕捉异常结束"。
"""


def catchError(_list, index):
    try:
        print(_list[index])
    except IndexError:
        print("序列边界越界")
    except (AttributeError, TypeError, SyntaxError):
        pass
    finally:
        print("捕捉异常结束")


mylist1 = ['jack', 18, 178]
catchError(mylist1, 3)
