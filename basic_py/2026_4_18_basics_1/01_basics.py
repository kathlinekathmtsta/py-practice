print("hello world")
# 我是单行注释

"""
在三引号中的注释被称之为多行注释
引号必须成对出现,要么全是双引号，要么全是单引号

"""
# 数据类型

int_num = 1024
float_num = 3.14
str_num = "hello world"
bool_num = True

print(type(int_num))
print(type(float_num))
print(type(str_num))
print(type(bool_num))
print(type(200))

# 内置函数 print-打印 type查看数据类型

# 打印表达式-计算公式计算出的结果
print(100+200)
print('100' + '200' + '300')
print('100 + 200 + 300')
# 字符串拼接，空格也是字符串

# print答应多个值
a = 100
b = 200
c = 300
print(a, b, c)

"""
字符串格式化
将变量的值带入字符串里

"""
str_data = "小明今年10岁"
print(str_data)
name = '小红'
age = 12
str_data = '%s今年%d岁' % (name, age)
print(str_data)

# f表达式 更简单
name = '小蓝'
age = 16
str_data = f'{name}今年{age}岁'
print(str_data)

# f表达式 更简单
name = 'anna'
age = 16
email_address = 'anna.@163'
str_data = f'{name}今年{age}岁,邮箱{email_address}'
print(str_data)

#浮点类型格式化

num = 3.1415926

# 保留小数点两位输出
str_data = '圆周率：%.2f' % num  # 支持四舍五入
print(str_data)

str_data = f'圆周率：{num:.2f}'
print(str_data)

num = 3.148321
# 字符串截取（不四舍五入）
s = str(num)
result = s[:s.index('.')+3]   # 截取到小数点后两位
print(result)

# 数学计数法
result = int(num * 100) / 100
print(result)
