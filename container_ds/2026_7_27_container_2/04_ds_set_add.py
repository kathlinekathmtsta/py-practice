int_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

#   添加元素
int_set.add(11)
print(int_set)
#   打印结果有序是编译器问题 集合本身是无序的

#   删除元素
int_set.remove(10)
print(int_set)

#   批量添加
int_set.update({11, 12, 13, 14})
int_set.update(['15', '16', '17'])
print(int_set)

#   随机弹出一个元素
data = int_set.pop()
print(data)
#   pop默认返回最后一个元素 但是集合无序 随机弹出

#   集合元素必须是不可变对象/可哈希对象
#   允许数据类型 int str float bool tuple
data_set = {1, '2', 3.14, False, (1, 2, 3)}
print(data_set)

#   可变对象 列表list 集合set 不能作为集合元素
#   data_set = {[1, 2, 3], {'name': 'anna'}}
#   print(data_set)
