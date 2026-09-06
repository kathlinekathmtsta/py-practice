#   拆包
nums = [1, 2, 3, 4]
# num_1 = nums[0]
# num_2 = nums[1]
# num_3 = nums[2]
# num_4 = nums[3]
# print(num_1, num_2, num_3, num_4)

num_1, num_2, num_3, num_4 = nums
print(num_1, num_2, num_3, num_4)

# 变量位置需要和列表中的元素位置保持一致
# 变量个数与列表中的元素个数保持一致

#   集合拆包 无法保证元素的位置赋值
int_set = {item for item in range(1, 5)}
num_1, num_2, num_3, num_4 = int_set
print(num_1, num_2, num_3, num_4)

# 可以使用拆包完成数据的位置互换
a = 1
b = 2
a, b = b, a
print(a, b)

#  字典拆包遍历
stu_info = {"name": "张三", "age": 18}
for key, value in stu_info.items():
    print(key, value)

d = {"a": 1, "b": 2}
# 不拆包写法
for i in d.items():
    print(i)   # 输出 ('a',1)  ('b',2)

# 拆包写法（最常用）
for k, v in d.items():
    print(k, v)  # 输出 a 1  、 b 2
