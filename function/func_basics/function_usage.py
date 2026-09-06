#   例题1-使用函数打印虚线，通过另外一个函数去控制打印虚线的次数


def print_one_line():
    print('-' * 30)


def print_num_line(num):
    i = 0
    while i < num:
        print_one_line()
        i += 1


# 调用示例，打印3行虚线
print_num_line(3)

#   例题2-计算三个数的和以及平均值


def add_num(n1, n2, n3):
    print(f'相加结果为：{n1 + n2 + n3}')
    return n1+n2+n3


def avg_num(n1, n2, n3):
    total = add_num(n1, n2, n3)  # 外层函数接收到的参数可以直接传递给内部的嵌套函数
    print(f'平均值为：{total / 3:.2f}')


avg_num(5, 7, 22)
