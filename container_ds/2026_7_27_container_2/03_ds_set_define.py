"""
集合特征：
1.无序性：集合中的元素没有顺序
2.唯一性：集合中的元素不能重复
3.可变性：集合中的元素可以修改
"""

nums = {100, 200, 300}
print(nums)
print(type(nums))

#   集合的迭代 结果无序 不能使用索引下标和切片
for num in nums:
    print(num)

nums = set()  # set() 空集合
print(type(nums))

nums = {}  # 返回字典类型
print(type(nums))

nums = {100, 200, 300}
# print(nums[:5]) 集合无序

nums = {100, 100, 200, 300, 300}
print(nums)
