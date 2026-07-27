str_data = 'abcdef'

print(str_data[0])
#   字符串下标开始位置为0
print(str_data[2])
print(str_data[5])

print('-' * 30)

print(str_data[-1])
print(str_data[-2])
print(str_data[-6])
print('-' * 30)
"""
字符串的索引取值 一次取一个
    str_data[索引值]

如果取值方向是从右到左则可以使用负数
    str_data[-1]是获取这个字符串的最后一个元素
"""

"""
字符串切片 获取字符串中的部分数据
str_data[起始位置(不写默认为0):结束位置:步长(不写默认为1)]

range(1,10) 在range这个内置函数中不包括结束位置本身
如果要取到字母c那么需要获取到这个字母的下标并 + 1
"""

str_data = 'abcdef'
print(str_data[1:3])
#   左闭右开 结束位置不包含本身
print(str_data[1:-1])
#   -1最后一个元素的前一个元素
print(str_data[2:])
#   结束位置不写可以获取到最后一个元素
print(str_data[:3])
print(str_data[:4:2])
print('-' * 30)

# 步长为负数的情况
# 取值方向是从右到左
print('步长为负数的情况：', str_data[4:1:-1])

# 获取字符串中的左右字母
print(str_data[:])
print(str_data[::])
print('-' * 30)
print(str_data[::-2])
print(str_data[::-1])
