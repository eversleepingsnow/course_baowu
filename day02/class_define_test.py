# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> class_define_test.py
# @Description   : **
# @Time          : 2021/7/18 9:44 
# @Author        : ly
"""用户自定义类"""


class Worker:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # 定义方法
    # 无参
    def getdetails(self):
        return "details = " + self.name + " " + str(self.salary)

    # 有参
    def getbonus(self, basepay):
        return self.salary + basepay


jack = Worker('jack', 5000)
print(jack)
print(jack.getdetails())
print(jack.getbonus(800))