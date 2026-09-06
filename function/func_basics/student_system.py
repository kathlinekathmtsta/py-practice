""""
学生管理系统个基础功能
1.打印操作菜单
2.添加学生信息
3.删除学生信息
4.修改学生信息
5.查询指定学生
6.查询所有学生
7.系统退出功能
"""
# 全局变量：存储学生信息的列表
info_list = []

current_id_counter = 0
# 全局变量：ID生成计数器（工程化方案：内存自增）
# 只要程序不关闭，这个ID就会一直增加，保证唯一


def print_menu():
    print("-" * 30)
    print(" 学生管理系统 V1.0")
    print(" 1:添加学生")
    print(" 2:删除学生")
    print(" 3:修改学生")
    print(" 4:查询学生")
    print(" 5:显示所有学生")
    print(" 6:退出系统")
    print("-" * 30)


def add_new_info():
    """添加学生信息"""
    global current_id_counter   # 声明我们要修改外部的全局计数器
    new_name = input("请输入姓名: ")
    new_tel = input("请输入手机号: ")
    new_qq = input("请输入QQ: ")

    # 核心逻辑先加1，再赋值。保证ID从1开始且永不重复
    # 保证 ID 从 1 开始，并且符合人类计数的直觉。
    current_id_counter += 1
    new_id = current_id_counter

    # 定义字典存储信息
    info = {
        "id": new_id,
        "name": new_name,
        "tel": new_tel,
        "qq": new_qq
    }

    info_list.append(info)  # 往学生列表的末尾追加 1 个元素
    print(f"添加成功！学号:{new_id}, 姓名:{new_name}")


def del_info():
    """删除学生信息"""
    del_num = input("请输入要删除的学号:")

    # 增加异常处理，防止用户输入非数字导致程序崩溃
    # 判断字符串里的内容是不是纯数字,是返回true.负数小数识别不了
    if not del_num.isdigit():
        print("输入错误，请输入数字！")
        return

    del_id = int(del_num)

    # 遍历查找要删除的学生
    for info in info_list:
        if info['id'] == del_id:
            del_flag = input(f"确认删除 {info['name']} 吗？(y/n): ")
            if del_flag == 'y':
                info_list.remove(info)
                print("删除成功！")
            else:
                print("已取消删除。")
            return  # 找到并处理完后，直接结束函数

    # 缩进与for对齐 只有当上面的 for 循环完整跑完，没遇到 return
    # 程序才会走到这里。这意味着：找遍了所有人，都没找到。
    print("查无此人，删除失败。")


def modify_info():
    """修改学生信息"""
    modify_num = input("请输入要修改的学号: ")
    # 防御性机制 误输入了字母 abc 或者空格，int("abc") 会导致程序崩溃
    if not modify_num.isdigit():
        print("输入错误：请输入数字！")
        return

    #   强制转换。input()函数接受字符串string文本，列表数据要求是整数
    modify_id = int(modify_num)

    for info in info_list:
        if info['id'] == modify_id:
            print(f"找到学生: {info['name']}，请输入新信息：")
            new_name = input("新姓名: ")
            new_tel = input("新手机号: ")
            new_qq = input("新QQ: ")

            # 更新字典内容
            info['name'] = new_name
            info['tel'] = new_tel
            info['qq'] = new_qq

            print("修改成功！")
            return

    print("查无此人，无法修改。")


def search_info():
    """查询学生信息"""
    search_name = input("请输入要查询的学生姓名: ")

    found = False
    for temp_info in info_list:
        if temp_info['name'] == search_name:
            print("查询到的信息如下：")
            # f-string 格式化输出表格线
            print(f"学号:{temp_info['id']}\t姓名:{temp_info['name']}\t手机:{temp_info['tel']}\tQQ:{temp_info['qq']}")
            found = True

    if not found:
        print("没有您要查找的信息...")


"""
利用标志位记分牌 found 记忆作用 会查出重名的人
针对重名情况 必须遍历完所有重名的人 中途不能停下
开始假设没找到
每找到一个把牌子翻过来 found = True
循环结束 如果是false则查无此人
"""


def print_all_info():
    """打印所有学生信息"""
    print("-" * 50)
    print(f"{'序号':<5}{'学号':<5}{'姓名':<10}{'手机号':<15}{'QQ':<15}")  # 简单的对齐
    print("-" * 50)

    i = 1
    for temp_info in info_list:
        print(f"{i:<5}{temp_info['id']:<5}{temp_info['name']:<10}{temp_info['tel']:<15}{temp_info['qq']:<15}")
        i += 1
    print("-" * 50)


def main():
    while True:
        print_menu()
        option = input("请选择操作: ")

        if option == '1':
            add_new_info()
        elif option == '2':
            del_info()
        elif option == '3':
            modify_info()
        elif option == '4':
            search_info()
        elif option == '5':
            print_all_info()
        elif option == '6':
            print("感谢使用学生管理系统，再见！")
            break
        else:
            print("输入有误，请重新输入")


if __name__ == '__main__':
    main()
