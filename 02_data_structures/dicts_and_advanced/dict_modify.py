person = {
    "name": "anna",
    "age": 18,
    "home": "usa"
}

#   增加 当key不存在 创建新的键值对 key:value
person['address'] = "new york"
print(person)

#   key存在则覆盖原有的数据
person['age'] = "20"
print(person)

#   del 删除指定键值对
del person['address']
print(person)

#   pop 弹出字典中最后一个键值对 popitem

stu_info = person.popitem()
print(stu_info)  # 返回的是元组中的元素 key,value

#   弹出指定的value
name = person.pop('name')
print(name)
print(person)

#   clear 清空字典内部元素 字典本身还存在
person.clear()
print(person)
