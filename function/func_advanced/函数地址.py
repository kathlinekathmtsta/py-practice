# 如何获取一个函数的内存地址

def solution1():
    pass


obj = None

print(id(solution1))
"""
函数引用
id(solution1) 不加括号 获取函数对象solution本身的内存地址

函数引用：指的是这个函数 本身 （拿着函数的身份证 或电话号码）。
函数调用：指的是 执行 这个函数（打这个电话）。
"""

print(id(solution1()))

"""
id(solution()) 函数调用call 加括号=运行函数体内部代码
函数体是 pass，并且没有 return 语句，执行后默认返回None
id 取的是返回值None的地址
"""

print(id(obj))
# 所有的None都指向同一个内存地址 id一致


def solution2():
    print('这是一个测试函数')


print(id(solution2))
# 打印函数对象本身的内存地址（不加括号）

work = solution2
print(id(work))
# work和solution 指向同一个对象 id相同

work()
# 调用= 执行 work 指向的函数
