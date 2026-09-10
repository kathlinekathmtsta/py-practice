# 星号拆包

def student_info(stu_id, name, cls_name):
    print(f'stu_id: {stu_id}, name: {name}, cls_name: {cls_name}')


stu_list = [10010, '安娜', '一班']
# student_info(stu_list[0], stu_list[1], stu_list[2])


student_info(*stu_list)

"""
* 在函数调用时，是解包操作符
列表中的元素位置必须和函数位置保持一致

*stu_list就是把列表 拆开，把元素一个个拿出来，当成独立的位置参数传给函数。
它等价于：
student_info(10010, '安娜', '一班')
"""

# 双星拆包
info = {
    'name': '安娜',
    'age': 18
}


# 字典中的key必须和参数名称保持一致才能完成拆包传参
def work(name, age):
    print(f'name: {name}, age: {age}')


work(**info)
# **info 的作用：把字典里的所有键值对拆成命名参数进去。
# 相当于 work(name='安娜', age=18)
