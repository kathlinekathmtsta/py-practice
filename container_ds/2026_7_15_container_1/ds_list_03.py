#   数据删除
movie_names = ['加勒比海盗', '骇客帝国', '第一滴血', '指环王', '霍比特人', '速度与激情']
print(movie_names)
# del是python中的关键字，可以删除任意对象，包括列表和列表元素
del movie_names[3]  # 会影响到原有列表的值
print(movie_names)

# pop: 将列表中最后一个元素弹出并可以赋值给一个新的变量
movie_name = movie_names.pop()  # pop操作 弹出
print('列表:', movie_names)
print('变量:', movie_name)
movie_name = movie_names.pop(2)  # 指定想要弹出元素下标
print('列表:', movie_names)
print('变量:', movie_name)

#   del pop 指定下标删除
#   remove: 指定元素名称删除
print(movie_names)
movie_names.remove('骇客帝国')
print(movie_names)
