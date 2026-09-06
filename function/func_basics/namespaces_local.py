#   函数嵌套
def work_1():
    print(1)


def work_2():
    print(2)
    # 在work_2函数内部调用work_1
    work_1()


work_2()

"""
内置命名空间：在任意py文件中都可以执行内置函数，内置函数存储在内置命名空间中
全局命名空间：在本文件中定义的变量可以在本文件中使用，一般不能跨文件使用
局部命名空间：某一个变量在某一个函数中创建那么只有这个函数能使用这个变量
"""


def test(num):
    def wrapper():
        print(num)
    return wrapper


func = test(10)
func()

# 全局变量
# 在当前文件中的任意代码片段都可以访问到这个变量中的值
num = 10


def work_3():
    print(num)


"""
先从函数内部查询是否存在这个变量
如果有直接用
如果没有则查询这个py文件中是否存在这个变量
"""


def work_2():
    num = 5
    print(num)


work_1()
work_2()
