stu_info = {
    'user': 'admin',
    'password': '123456'
}

#   1.获取变量key
print("=== 遍历所有 key ===")
for key in stu_info:
    print(key)

#   2.用 keys() 方法获取所有 key
#   dict_keys对象，支持迭代，类似列表行为
print("\n=== 用 keys() 获取所有 key ===")

keys = stu_info.keys()
print(list(keys))  # 转成 list 打印key

#   3.用 values() 方法获取所有 value dict.values
print("\n=== 用 values() 获取所有 value ===")
print(stu_info.values())
print(list(stu_info.values()))  # 转成 list 打印 value

#   4.用 items() 方法获取所有 key-value对
print("\n=== 用 items() 获取所有 key-value 对 ===")
print(stu_info.items())
print(list(stu_info.items()))  # 转成 list 打印

#   5.获取每一个 key: value
for key, value in stu_info.items():
    print(key, value)

"""
dict 内置方法 get 
获取字典中的指定value值 
"""
print("\n=== get方法获取字典中的指定value值 ===")
person = {
    "name": "anna",
    "age": 18,
    "home": "usa"
}

print(person['home'])
# print(person['gender']) key不存在会报错
print(person.get('gender'))
# get获取不存在的key 返回默认值空值none
