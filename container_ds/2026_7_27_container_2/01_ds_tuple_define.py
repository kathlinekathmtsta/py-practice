#   元组与列表类似 都支持存储值以及迭代for循环
#   区别 元组中的元素不能被修改 没有添加/删除内置方法

int_tuple = (1, 2, 3)
print(type(int_tuple))

int_tuple = tuple()  # 声明空元组
print(type(int_tuple))

int_tuple = (1)  # 整数
print(type(int_tuple))
int_tuple = (1,)  # 元组中元素只有一个时 要加上逗号
print(type(int_tuple))  # type 返回变量的数据类型
int_list = [1]  # 列表只有一个元素时 不用加逗号
print(type(int_list))

#   验证tuple不能被修改
int_tuple = (1, 2, 3)
#   int_tuple[0] = 4 元组中元素修改时会报错

#   元组内置方法 统计 index count
print(int_tuple.count(2))   # 统计元素出现次数
print(int_tuple.index(2))   # 获取元素索引

#   元组支持切片
int_tuple = (1, 2, 3, 4, 5)
new_tuple = int_tuple[:4]
#   切片结果返回一个新元组 不会影响原元组
print(new_tuple)
