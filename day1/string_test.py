import sys

'''
多行注释


# sys.stdout.write("\n")
print("hake", end="")  # end空串标识不换行
sys.stdout.write("\n")
# 写文件 不能追加写入
# myFilePath = open("d:/abc.txt", "w")
# print("hello word ", "hehehe", file=myFilePath)  # 重定向输出

# 读文件
file = open("d:/abc.txt")
# filestr = file.read()
print(file.readline())
# print(filestr)
'''

# string 应用
'''
myStr = "abcdefg"
print(len(myStr))
print(myStr[3])
print(myStr[-3])
print(myStr[len(myStr)-3])
print(myStr[:3])
print(myStr[1:3])
print(myStr[:])
print(myStr[:-1])
print(myStr*2)
print(myStr[::-1])
print(myStr[5:1:-1])
'''
'''字符串不可变性'''
myStr = '''
11111
22222
'''
print(myStr)

token = "111,222,333,444"  # csv
tokenList = token.split(',')  # 以逗号分隔返回字符串列表 ['111', '222', '333', '444']
print(tokenList)
print(len(tokenList))  # 列表长度=4
print(ord('\n'))  # 显示回车不可见字符的ascii 10
otherStr = '12345678ddDD'
# 拼接
print('2' + otherStr[1:len(otherStr)])
# 查找
print(otherStr.find('23'))
# 替换
print(otherStr.replace("12", "rt"))
# join
print(" ".join(otherStr))
print(otherStr.join("join"))
# upper
print(otherStr.upper())
# lower
print(otherStr.lower())
# is
print(otherStr.isalpha(), otherStr.isspace())
#
