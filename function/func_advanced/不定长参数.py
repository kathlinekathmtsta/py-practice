def demo_func(*args, **kwargs):
    print("args (元组):", args)
    print("kwargs {字典}:", kwargs)


demo_func(1, 2, 3, name="小明", age=18)


"""
*args： 类型为元组的不定长参数
**kwargs：类型为字典的不定长参数

*args：用来接收 多余的、没名字的 位置参数，把它打包成一个元组
**kwargs：用来接收 多余的、有名字的 关键字参数（key=value 形式），把它打包成一个字典

在函数定义时，如果这四种参数都出现，顺序必须严格遵循：
位置参数（普通形参） > *args > 缺省参数（默认值） > **kwargs

pass 检查语法是否正确
def func(a, b, *args, c=100, **kwargs):
    pass
"""


def my_func(*args):
    print(args)


my_func(1, 2, 3, 4)   # 输出：(1, 2, 3, 4)  接收了多个值


def add(a, b, c):
    print(a + b + c)


nums = [1, 2, 3]
add(*nums)   # * 负责 拆散 列表，相当于 add(1, 2, 3) 输出 6

"""
# *号 定义函数时 接收多个值   负责接收并打包成元组
# *号 调用函数时 拆散多个值   把 * 放在一个列表/元组前面 拆散成单个元素，当作位置参数传进去。
定义时 形参 加 * 打包 收进来  调用时 实参 加 * = 拆包 放出去
"""


# kwargs接收的参数必须是命名参数  key=value
def func_2(**kwargs):
    print(kwargs)


func_2(name='admin', sex='男')


# 顺序要求：必传位置参数 -> *args -> **kwargs
def test_attr(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)


test_attr(1, 2, 123, 456, 789, name='安娜')
