def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)


print(fib_recursive(10))  # 输出 55


def fib_iterative(n):
    if n <= 1:
        return n

    a, b = 0, 1  # 初始化前两个数
    for _ in range(2, n + 1):
        a, b = b, a + b  # Python 优雅的交换赋值
    return b


# 测试：计算第 50 个数
print(fib_iterative(50))  # 输出 12586269025

# 非递归用的比较多 递归容易写死循环
