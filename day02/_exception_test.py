# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> _exception_test.py
# @Description   : **
# @Time          : 2021/7/18 13:05 
# @Author        : ly
def getlistvalue(myList, index): return myList[index]


# 1.exception常用格式，一般抛出系统异常
def catchlistsafety():
    try:
        print(getlistvalue(myList, 4))
    except IndexError:
        print("index out of bound!")
    except NameError:
        pass
    except KeyError:
        pass
    # 多种异常合并处理
    except (AttributeError, TypeError, SyntaxError):
        pass
    else:  # 如果没有发生异常时做的动作
        print("get the list value!")
    # 始终会做finally
    finally:
        print("release memory!!")
    print("do the next action...")


myList = [123, 'abc', 4.56]
# 直接调用边界越界
# getListValue(myList,3)
catchlistsafety()
