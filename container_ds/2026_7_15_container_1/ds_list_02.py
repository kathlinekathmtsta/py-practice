#   列表的内置方法
stu_names = ['name1', 'name2', 'name3', 'name4']

#   append: 每次在列表的末尾添加一个元素
stu_names.append('name5')
print(stu_names)

#   extend: 可以批量添加多个元素 位置在原列表末尾
#   传递的参数要求是迭代对象-可以被for循环执行的对象
new_stu_list =['name5','name6','name7']
stu_names.extend (new_stu_list)
print(stu_names)

#   insert： 指定索引位置完成元素的插入
new_stu = 'teacher'
stu_names.insert (0,new_stu)
print(stu_names)

#   修改元素
stu_names[1] = 'anna'
print(stu_names)

#   查询元素 返回布尔值
stu_name = 'name1'
print(stu_name in stu_names)
stu_name = 'anna'
print(stu_name in stu_names)

if stu_name in stu_names:
    print('find')
else:
    print('not find')

#   count: 统计列表元素的个数
print(stu_names.count('anna'))  # 统计当前列表中 '安娜' 出现的次数
stu_names.append('anna')     # 向列表末尾添加一个元素 '安娜'
print(stu_names)
print(stu_names.count('anna'))


#   index: 返回你指定的元素的下标
print(stu_names.index('anna'))  # 返回了第一次出现的元素的下标
# print(stu_names.index('admin'))  # 如果元素不存在会报错
