#   函数隔离
def work_1():
    num = 200
    # num = 100
    # print('num_1:', id(num))
    return num


def work_2():
    num = 400
    # num = 100
    # print('num_1:', id(num))
    return num


# 打印函数在内存中的地址
print(id(work_1))
print(id(work_2))

print(work_1())
print(work_2())

#   相同值的变量地址可能相同   小整数池的预分配和重用
#   减少内存碎片和提高访问效率  仅适用于小整数对象对[-5,257]范围内
