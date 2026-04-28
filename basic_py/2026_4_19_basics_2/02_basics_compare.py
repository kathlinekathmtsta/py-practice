#  比较运算符
num1 = 10
num2 = 20
print(num1 > num2)
print(num1 < num2)

print(num1 >= num2)
print(num1 <= num2)

print(num1 != num2)

"""
在多个判断条件的场景下会使用逻辑运算符
and / &&（并且）所有条件全部成立则返回True
or  / ||（或者）其中一个条件成立则返回True
not / ! （非,取反） not(True)=False
"""
print('--------')

# and是用于链接多个条件并且要保证所有条件都为真才返回True
print(100 > 50 and 90 < 200)
print(100 < 50 and 90 < 200)

# or: 多个条件只要成立一个则整体条件返回真，所有条件都不成立则整体返回False
print(100 < 50 or 90 < 200)
print(100 < 50 or 90 > 200)

# not: 取反
print(100 > 90)
print(not 100 > 90)
print(not 100 < 90)
print('--------')
