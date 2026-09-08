#   用 * 和 / 来限制调用者传参 接口设计的防御性和API的稳定性

# 代码块1: 使用 * 强制指定命名参数  * 后面必须写清楚标签

def print_info_1(name, age, *, gender, address):
    print(f'name: {name}, age: {age}, gender: {gender}, address: {address}')


# * 后面必须使用命名参数的方式传参
print_info_1('admin', 18, gender='女', address='长沙')


# 代码块2: 使用 / 强制指定位置参数   / 前只能按顺序传递，不能写标签(具体的值)

def print_info_2(name, age, /, gender, address):
    print(f'name: {name}, age: {age}, gender: {gender}, address: {address}')


# 前两个参数（/前面的）只能使用 位置参数传参 不带变量名称

print_info_2('admin', 18, '女', '长沙')
