age = 17

print('if代码即将被执行...')
if age >= 18:
    # 如果条件成立则if内部的代码才会被执行
    print('已经成年...')
    print('可以去工作了...')
    print('可以去上网了...')

# 如果编辑的代码不在if判断的内部则不会受到if代码的管控
print('if代码执行完毕...')

"""
1.python关键字if是用来开启判断语句的
2.写完判断条件记得要加冒号(必须是英文状态下)
3.遇到冒号要缩进
4.被缩进的代码有受到if判断语句的执行管控
"""
local_name = 'admin'
local_password = '123456'

# 无论你输入的是字母还是数字，input() 函数永远都会把它当作字符串（String）处理
# input() 获取到的数字本身就是字符串类型，而你定义的密码 '123456' 也是字符串类型

username = input('请输入用户名：')
password = input('请输入密码：')

# if username == local_name and local_password == password:
#     print('登录成功...')
#
# print('if代码执行完毕...')

# 如果大家需要将密码强转为int类型则必须要保证密码中的数据是纯数字
# 类型匹配：输入的密码默认为字符串类型，若本地密码定义为整数（如123456），必须使用int()进行类型转换
# 转换限制：只有当密码为纯数字时才可转换为int类型，包含字母或特殊字符时将导致转换失败
# 实践建议：实际开发中密码应保持字符串类型，因其可包含数字、字母和特殊字符的组合

if username == local_name and local_password == password:
    print('登录成功...')
else:  # 如果条件不成立则执行else之下的代码
    print('登录失败...')

"""
if 条件:
    条件成立时会被执行的代码...
else:
    条件不成立时会被执行的代码...
"""