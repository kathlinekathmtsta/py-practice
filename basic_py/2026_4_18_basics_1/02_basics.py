#  input的运用 接收输入
# \t表示一个tab键的距离
print("hello \t world")
# input()：输入数据
username = input("Enter your name: ")  # python解释器执行到当前语句会等待用户在终端输入信息
print("Hello", username)
#  input可以监听用户在键盘上输入的信息并把信息赋值给一个变量

# 任务需求：让用户输入登录账号和登录密码并在终端打印用户的账号信息
username = input("请输入用户名：")
password = input("请输入密码：")
print(f"用户名为：{username}, 密码为：{password}")

"""
input所接收的数据全部都是字符串类型
输入数字也要自己转类型：int(input())
"""
num = input("请输入一个数字：")
print(num)
print(type(num))
