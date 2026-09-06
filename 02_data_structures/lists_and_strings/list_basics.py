#   列表的使用
stu_names = ['name1', 'name2', 'name3', 'name4']

#   列表支持迭代
for name in stu_names:
    print(name)
print('-' * 30)
print(stu_names[1])
print('-' * 30)

#   while循环对列表的迭代 len内置函数
list_length = len(stu_names)
i = 0
while i < list_length:
    print(stu_names[i])
    i += 1

#   列表元素的修改
stu_names[0] = 'anna'
print(stu_names)
print('-' * 30)

#   列表的切片 返回新列表 切片后不改变原列表
print(stu_names[1:3])
print('-' * 30)
new_list = stu_names[1:3]
print(new_list, stu_names)

#   列表的倒序
new_list = stu_names[::-1]
print(new_list, stu_names)

"""
python中有内置的几种数据结构：列表、字典、元组、集合
数据结构可以保存多个数据

list定义的方式：
    data_list = []  代表创建了一个空列表
    data_list = list()  代表创建了一个空列表"""

# 列表可以保存多个不同类型的数据
data_list = [1, 2, 3, 4, '123', 3.14, True, False]
print(data_list)

# 空列表的声明方式
data_list = []
print(data_list)

#   常用
data_list = list()
print(data_list)