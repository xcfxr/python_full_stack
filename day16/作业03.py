from functools import wraps
order_dict = {'0': 'break'}
init_order = {'0': 'break'}


def init(func):
    init_order[str(len(init_order))] = func

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper


def order(func):
    order_dict[str(len(order_dict))] = func

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def load_data():
    with open('db.txt', 'rt', encoding='utf-8') as f:
        for line in f:
            usr, pwd, balance, locked = line.split(' ')
            user_info[usr] = [pwd, int(balance), int(locked)]


@init
def register():
    while True:
        usr = input('请输入用户名：').strip()
        if usr in user_info:
            print('该用户名已被使用，请重新操作')
            return
        else:
            break
    while True:
        pwd = input('请输入密码：').strip()
        re_pwd = input('请再次输入密码：').strip()
        if pwd == re_pwd:
            print('注册成功，当前账户余额为0')
            user_info[usr] = [pwd, '0', 0]
            rewrite()
            break
        else:
            print('两次密码输入不一致，请重新输入！')


@init
def login():
    count = 3
    while True:
        usr = input('请输入用户名：').strip()
        if usr not in user_info:
            print('该用户名不存在，请先注册')
            break
        elif user_info[usr][2]:
            print('该账户被锁定，无法登录')
            break
        else:
            pwd = input('请输入密码：').strip()
            if pwd == user_info[usr][0]:
                global user
                user = usr
                print('登陆成功')
                while True:
                    for k, v in order_dict.items():
                        if k != '0':
                            print(k, v.__name__)
                        else:
                            print(k, v)
                    order = input('请输入指令：')
                    if order == '0':
                        break
                    if order in '1234':
                        order_dict[order]()
                    else:
                        print('请输入规范指令')


                break

            else:
                count -= 1
                if count != 0:
                    print('密码输入错误，请重新输入，输入次数达到三次将会锁定账户')
                    print('还剩%d次' % count)
                else:
                    print('输入错误次数打到三次，账户锁定')
                    user_info[usr][2] = 1
                    rewrite()
                    break


@order
def transfer():
    target = input('请输入汇款对象：').strip()
    if target not in user_info:
        print('该对象不存在')
    else:
        amount = input('请输入汇款金额：')
        if amount.isdigit():
            amount = int(amount)
            if amount <= user_info[user][1]:
                user_info[user][1] -= amount
                print('汇款成功， 账号还剩%d元' % user_info[user][1])
                user_info[target][1] += amount
                rewrite()
            else:
                print('余额不足，汇款失败')
        else:
            print('金额必须为数字， 汇款失败')


@order
def withdraw():
    amount = input('请输入取钱金额：').strip()
    if amount.isdigit():
        amount = int(amount)
        if amount <= user_info[user][1]:
            user_info[user][1] -= amount
            print('取钱成功， 账号还剩%d元' % user_info[user][1])
            rewrite()
        else:
            print('余额不足，取钱失败')
    else:
        print('金额必须为数字， 取钱失败')


def rewrite():
    with open('db.txt', 'wt', encoding='utf-8') as f:
        for usr, info in user_info.items():
            f.write(usr)
            for each in user_info[usr]:
                f.write(' ')
                f.write(str(each))
            f.write('\n')


@order
def query():
    print('当前余额为%d' % user_info[user][1])


@order
def recharge():
    amount = input('请输入充值金额：').strip()
    if amount.isdigit():
        amount = int(amount)
        user_info[user][1] += amount
        print('充值成功， 账号还剩%d元' % user_info[user][1])
        rewrite()
    else:
        print('金额必须为数字， 充值失败')


if __name__ == '__main__':
    user_info = {}
    load_data()
    user = None
    while True:
        for k,v in init_order.items():
            if k != '0':
                print(k, v.__name__)
            else:
                print(k, v)
        order = input('请输入指令：')
        if order == '0':
            break
        if order in '12':
            init_order[order]()
        else:
            print('请输入规范指令')
