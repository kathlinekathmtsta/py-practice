"""
布尔类型只有两个值：True（真）和 False（假）
if 条件: 后面跟条件判断，条件为 True 时执行下面缩进的代码块
else: 表示“否则”，当 if 的条件为 False 时，执行 else 下面的代码块
"""

# 条件为真
have_money = True
print(have_money)

if have_money:
    print('你真有钱')
else:
    print('你是真穷')

# 测试 False 情况
have_money = False
if have_money:
    print('你真有钱')
else:
    print('你是真穷')
