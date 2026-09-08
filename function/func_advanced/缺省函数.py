#   缺省参数是 定义参数的过程中创建了默认值


def print_info(name, age=18):
    print(name, age)


print_info('admin')
print_info(name='安娜', age=48)


def print_info(name, age=18, address='长沙'):
    print(name, age, address)


print_info('安娜')


"""
缺省参数的作用：
    1.可以对参数设置默认值
    2.如果在调用函数的过程中没有传递具体的值则使用默认值
    3.如果在调用函数的过程中传递了新的参数则使用新参数
"""
