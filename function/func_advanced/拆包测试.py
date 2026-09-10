# 字典get 获取key value

info = {
    'name': '安娜',
    'age': 18
}


# 工程化：直接明确写清需要什么参数
def work(name, age):
    print(f'name: {name}, age: {age}')


# 调用时直接拆包传参
work(**info)

info = {
    'name': '安娜',
    'age': 18
}


# 工程化：统一用 **kwargs 接收，并在内部规范提取
def work(**kwargs):
    # 工程上通常不直接用 kwargs.get()，而是先定义一个规范的数据结构
    name = kwargs.get('name', '未知')  # 提供兜底默认值
    age = kwargs.get('age', 0)

    print(f'name: {name}, age: {age}')
    # 如果有其他多余参数，通常也要处理掉，而不是默默吞掉
    # 比如打日志记录那些不认识的参数：extras = {k:v for k,v in kwargs.items() if k not in ['name', 'age']}


# 调用时直接拆包传参
work(**info)
