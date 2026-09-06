def add_num(num_1, num_2):
    return num_1 + num_2
    # 可以将计算结果返回出去并赋值给一个变量


def sub_num(num_1, num_2):
    return num_1 - num_2


result = add_num(9, 2)
result = sub_num(result, 10)
print(result)

"""
如果第二个函数在计算的过程中需要获取第一个函数的最终结果完成计算
那么就可以通过return返回最终结果并将结果传递给第二个函数

当函数内部不写return语句时，Python解释器会自动在函数末尾添加return None

返回值 是函数在执行完逻辑代码后产生的最终结果
作用: 将函数计算结果传递给外部变量 使用return关键字将结果返回并赋值给变量
return将函数结果用于后续计算或传递给其他函数时使用
"""


#   Python列表 insert、 append、 remove、 sort
#   都是原地修改，返回 None，不要套在 print 里面直接打印调用结果！

list_data = [1, 2, 3]
# 在索引0位置插入4
ret = list_data.insert(0, 4)

print(ret)   # 输出 None 有insert 返回None
print(list_data)    # 输出 [4, 1, 2, 3]，原列表已经被改动

list_data.insert(0, 4)   # 执行插入，原地改列表
print(list_data)


#   在函数中使用分支

def check_num(num):
    if num == 100:
        return num + 1
    elif num == 200:
        return num + 2
    else:
        return 300


print(check_num(100))
print(check_num(200))
print(check_num(123))


#   通过return返回多个值
def return_num():
    return 1, 2, 3
#   return返回多个值则会打包成一个元组 因为元组特性元素不可变


result = return_num()
print(result)

#   拆包分别取出元组中的元素 赋值方法
r1, r2, r3 = return_num()
print(r1, r2, r3)
