# 匿名函数本质上就是没有函数名称的函数
"""
没有函数名称，返回一个结果无需手写return关键字
匿名函数的主要作用是：将匿名函数作为一个参数传递给其他的函数
匿名函数能完成的功能普通函数都能完成，但是占用的内存更小，并且用完直接释放
"""

# 直接调用，不存名字 用完就丢
result = (lambda a, b: a + b)(1, 2)
print(result)

# 使用匿名函数完成列表元素排序 按年龄从大到小排序

stu_list = [
    {"name": "顾安", "age": 18},
    {"name": "夏洛", "age": 19},
    {"name": "木木", "age": 17}
]

# reverse=True 从大往小排
stu_list.sort(key=lambda item: item["age"], reverse=True)

print(stu_list)


# 等价于
def my_sort(item):
    return item["age"]


stu_list.sort(key=my_sort, reverse=True)
# 送人头内部已经实现了对列表元素的迭代
print(stu_list)

