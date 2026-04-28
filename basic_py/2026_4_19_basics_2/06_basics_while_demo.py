i = 0  # 步过
while i < 10:
    print(i, end=' ')  # 空格分隔，不换行
    i += 1
print()
# 执行一次计数器 + 1，加到一定次数可以让循环终止
# 死循环现象产生原因：忘记写计数器递增语句时，条件永远成立（如i恒为1且i <= 5）

# 计算1 - 100序列中的元素除以3余数为0和除以7余数为0的累加和
num_result = 0
i = 1
while i <= 100:
    if i % 3 == 0 and i % 7 == 0:
        num_result += i
    i += 1
# 21,42,63,84
print("="*20)
print(f"1-100中能同时被3和7整除的数累加和：{num_result}")
print("="*20)

size = 5
line = '*' * size  # 生成包含5个*的字符串：'*****'
count = 0
while count < size:
    print(line)     # 每次循环打印一行*****
    count += 1      # 计数器+1，避免死循环
print("="*20)

# 打印上三角形
size = 5
row = 1
while row <= size:
    col = 1
    while col <= row:  # 关键修改：col <= row
        print('*', end=' ')  # 打印完换行
        col += 1
    print()  # 强制换行
    row += 1
