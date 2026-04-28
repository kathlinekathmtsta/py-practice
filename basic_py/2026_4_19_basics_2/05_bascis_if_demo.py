chepiao = True
daoju = 11

if daoju <= 9:
    print('安检通过...')
    # if chepiao == True:
    if chepiao:
        print('已有车票，可以上车...')
    else:
        print('暂无车票，禁止上车...')
else:
    print('危险，禁止进站...')

chepiao = False
daoju = 9

if daoju <= 9:
    print('安检通过...')
    # if chepiao == True:
    if chepiao:
        print('已有车票，可以上车...')
    else:
        print('暂无车票，禁止上车...')
else:
    print('危险，禁止进站...')

"""
if...elif...else

if 条件1:
    条件1成立要执行的代码
elif 条件2:
    条件2成立要执行的代码
elif 条件3:
    条件3成立要执行的代码
    ...
else:
    以上条件都不成立则执行else之下的代码

"""
# 判断一位学生考试的分数位于哪个等级
score = 77
if 90 <= score <= 100:
    print('本次考试，等级为A')
elif 80 <= score < 90:
    print('本次考试，等级为B')
elif 70 <= score < 80:
    print('本次考试，等级为C')
elif 60 <= score < 70:
    print('本次考试，等级为D')
elif 0 <= score < 60:
    print('本次考试，等级为E')
else:
    print("分数有误...")
