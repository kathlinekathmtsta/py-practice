#   1.字符串内置查找类 find rfind cout
#   字符串内置方法 print(变量名.方法名(参数))

#   find  返回的结果是当前英文单词的首字母索引
my_str = 'welcome to www.tulingxueyuan.com'
print(my_str.find('to'))

# rfind: 从右往左查询
print(my_str.rfind('to'))

# count: 统计出现的元素次数
print(my_str.count('w'))


#   2.字符串内置修改替换类 replace lower upper

""" 常用replace: 字符串替换 """
print(my_str.replace('w', 'W'))
print(my_str.replace('w', 'W', 1))
#  替换1次 W替换掉第一个w

# lower: 将字符串中的元素全部转为小写
my_str = "WELCOME to www.tulingxueyuan.com"
print(my_str.lower())

# upper: 将字符串中的元素全部转为大写
print(my_str.upper())

#   tiltle 每个单词的首字母转为大写，其余字母全部小写
my_str = "welcome TO www.tulingxueyuan.com"
print(my_str.title())


#   3.字符串内置分割拼接类 split('分隔符') partition('分隔符')

""" 经常用split: 字符串分割 分割出来的结果是一个列表中的元素" """
my_str = 'welcome to www.tulingxueyuan.com'
print(my_str.split(' '))
print(my_str.split(' ')[0])

# partition: 字符串分割只分割一次，返回三元组 (左边,分隔符,右边)
print(my_str.strip().partition('to'))

# splitlines: 根据行分割
my_str = """
welcome to www.tulingxueyuan.com
thank you
good good study day day up
"""
print(my_str.splitlines())


#   4.字符串内置查找类startswith  endswith 返回 true/false

# startswith: 判断你输入字符串是否是另外一个字符串的开头
print(my_str.startswith('w'))
print(my_str.startswith('a'))
print(my_str.startswith('welcome'))

# endswith: 判断你输入字符串是否是另外一个字符串的结尾
print(my_str.endswith('m'))
print(my_str.endswith('w'))


#   5.字符串去除空白类strip

# strip: 删除字符串两端的空白字符
my_str = "  welcome to www.tulingxueyuan.com  "
print(my_str)
print(my_str.strip())


""" 6.join方法
    在字符串列表的每个元素后面插入指定连接符，构造新的字符串
    格式  "连接符".join(可迭代对象)
"""
str_list = ['welcome', 'to', 'www.tulingxueyuan.com']
str_join = '-'
print(str_join.join(str_list))
# 使用空格拼接
print(" ".join(str_list))
# 使用加号拼接
print("+".join(str_list))

my_str = "welcome-to-www.tulingxueyuan.com"
# 字符串切分成列表
lst = my_str.split('-')
# 列表拼接回字符串
new_str = '-'.join(lst)
print(new_str)
