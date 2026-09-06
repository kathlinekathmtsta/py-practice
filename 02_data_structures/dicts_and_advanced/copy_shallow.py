"""
浅拷贝 只能拷贝不可变数据 无法拷贝可变对象
"""

#   不建议操作 地址相同 列表外部值修改影响原本的数据
name_list = [['张三', '李四'], '王五', '赵六', '钱七']
new_name_list = name_list
print(f'name_list: {id(name_list)}')  # id获取地址
print(f'new_name_list: {id(new_name_list)}')

# 修改嵌套子列表内部元素
name_list[0][0] = '安娜'
print(f'name_list: {name_list}')
print(f'new_name_list: {new_name_list}')

#   输出结果一样 原因 new_name_list 只是原列表的引用，
#   两者指向同一块内存， 修改原列表里的值，两个变量都会同步变化。

"""
将原有的数据进行备份
做法 拷贝数据 新开辟一块内存 保存最开始的列表
"""

print(f'new_name_list: {id(new_name_list[0])}')
print(f'new_name_list: {id(name_list[0])}')
print('-' * 30)
print(f'new_name_list: {id(new_name_list[1])}')
print(f'new_name_list: {id(name_list[1])}')


new_name_list[0][0] = '安娜'
print(f'new_name_list: {new_name_list}')
print(f'name_list: {name_list}')
print('-' * 30)

"""
浅拷贝用 .copy() 只复制了最外层列表 不可变
里面嵌套的子列表 [张三,李四] 还是共用同一个内存地址 需要深拷贝
浅拷贝了一个嵌套列表，修改内层列表中的值会对原有列表造成影响
"""
