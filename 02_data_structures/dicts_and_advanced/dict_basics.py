#   字典dict

stu_info_dict = {
    'username': '张三',
    'age': '17',
    'home': 'usa'
}
print(stu_info_dict['username'], stu_info_dict['age'])
print(stu_info_dict['home'])

"""
字典 = {
    key: value,
}

键值对需要通过冒号进行分割
一个键值对就是字典的一个元素
元素与元素之间需要通过逗号分割

"""

#   字典遍历
#   字典中的ket必须唯一 是不可变对象

stu_info = {
    'name': '安娜',
    'age': 18,
    'gender': '女',
    'address': '长沙'
}

#   方法1 返回值是字典的key 没有value
for item in stu_info:
    print(item)

#   方式2：使用 items()"

for key, value in stu_info.items():
    print(key, value)

#   字典结合其他数据结果嵌套
cls_info = {
    'stu_names': ['张三', '李四', '王五'],
    'stu_age': (18, 19, 20)
}

#   在字典中获取指定的value需要根据key获取
#   格式 cls_info['key_name']
print(cls_info['stu_names'])
print(cls_info['stu_age'])

#   常见场景  key常见 作为列表保存[]
stu_info = [
    {'user_name': '安娜'},
    {'user_name': '双双'}
]

for item in stu_info:
    print(item['user_name'])


"""
1.字典的key必须唯一且不可变
2.数据结构灵活，可与其他容器类型嵌套
3.直接遍历只能获取键key，无法获取值value
"""
