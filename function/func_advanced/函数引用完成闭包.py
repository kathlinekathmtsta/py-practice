def work(func_obj):
    def wrapper():
        print('准备执行函数...')
        func_obj()  # 执行 传进来的原函数 test_method
        print('测试函数执行完毕...')
    return wrapper

# work 函数就像包装器，可以在不修改原函数（test_method）内部代码的前提下，给它套上一层额外的功能（前后打印日志）


def test_method():
    print('这是一个测试函数')


wra_func = work(test_method)
# 将test_method 作为参数传给了func_obj
# 函数引用，没有小括号 test_method（） 函数并没有运行

wra_func()
# 调用了 wrapper()
# 调用work函数 最后 return wrapper的结果，被赋值给了变量 wra_func
# 此时 wra_func 拿到的就是 wrapper 函数本身的引用（地址）
