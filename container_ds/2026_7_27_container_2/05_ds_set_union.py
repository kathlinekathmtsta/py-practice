#   集合的运算

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 交集 & 相同部分
print(set1 & set2)

#   并集 | 全部去重
print(set1 | set2)

#   差集运算 去除另一个集合里的重复部分
#   一个集合中移除另一个集合所包含的元素后 剩下的部分
result = set2 - set1
print(result)
result = set1 - set2
print(result)

#   对称差集 获取两个集合中不重复的所有元素
result = set1 ^ set2
print(result)
