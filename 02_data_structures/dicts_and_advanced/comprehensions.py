#   推导式 应用爬虫翻页
#   创建1-100的列表

int_list = []
for item in range(1, 101):
    int_list.append(item)
print(int_list)

#   方法2 列表推导式
int_list = [item for item in range(1, 101)]
#   每一次循环的结果放入item
print(int_list)

#   偶数序列
int_list = [item for item in range(1, 21) if item % 2 == 0]
print(int_list)

#   奇数序列    if条件判断或者步长控制
int_list = [item for item in range(1, 21) if item % 2 != 0]
print(int_list)
int_list = [item for item in range(1, 21, 2)]
print(int_list)

#   支持推导式：列表、集合、字典 不包括元组
int_data = (item for item in range(1, 11))
print(int_data)  # 输出生成器对象 而非元组数据

#   集合的推导式
int_set = {item for item in range(1, 11)}
print(int_set)  # 输出无序且去重的集合

#   字典推导式key-value 使用情况不多
int_dict = {item: item*item for item in range(1, 5)}
print(int_dict)  # 输出{1:1, 2:4, 3:9, 4:16}

#   推导式生成嵌套数据结构 复杂嵌套可读性差
int_list = [[x, y] for x in range(1, 3) for y in range(3)]
print(int_list)

int_list = list()
for x in range(1, 3):
    for y in range(3):
        int_list.append([x, y])
print(int_list)

"""
简单结构（单层循环）优先使用推导式
复杂结构（多层嵌套）改用显式for循环
专业数值计算建议使用NumPy库
"""