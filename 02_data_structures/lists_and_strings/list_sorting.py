#   列表排序

#   sort方法 修改原有列表的值
int_list = [1, 2, 3, 4, 5]
int_list.sort()  # 从小到大排序
print(int_list)

#   reverse: 反转
int_list.sort(reverse=True)
print(int_list)


int_list = [1, 2, 3, 4, 5]
int_list.reverse()
print(int_list)

#   python内置函数 sorted实现
new_list = sorted(int_list)
print(new_list)
#   返回一个重新排序的新列表 new_list

#   列表嵌套 每个小列表是大列表的一个元素
school_names = [
    ['北京大学', '清华大学'],
    ['南开大学', '天津大学', '天津师范大学'],
    ['山东大学', '中国海洋大学']
]

print(school_names[1])
print(school_names[1][2])
print(school_names[2][0])

int_list = [1, 2, 3, 4, 5]
int_list.insert(0, ['1', '2', '3']) 
print(int_list)
