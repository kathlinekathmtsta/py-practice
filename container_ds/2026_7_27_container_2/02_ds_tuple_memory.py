#   如何获取变量在内存中的地址
#   Python中的变量保存的是常量在内存所占用的内存地址

num = 1
print(id(num))
#   内置函数id获取保存的地址

#   元组中的元素不可修改的实质是 元素中的地址不能修改

data_tuple = (1, 2, 3, [4, 5])
print(f'修改前内存地址: {id(data_tuple[3])}')
data_tuple[3][0] = '4'  # 修改列表元素
print(f'修改后内存地址: {id(data_tuple[3])}')  # 地址不变
print(data_tuple)
