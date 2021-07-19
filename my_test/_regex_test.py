# -*- coding: utf-8 -*-
# @Project -> File   : course_baowu -> _regex_test
# @Description   : regex
# @Time          : 2021/7/19 13:55 
# @Author        : ly

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('455-555-4545')
print(mo.group())
print('---------------------------')
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d)')
mo = phoneNumRegex.search('455-555-4545')
print(mo.group(1) + '   ' + mo.group(2))
areaCode, mainNumber = mo.groups()
print(areaCode, mainNumber)


