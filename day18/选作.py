import os
import time
from functools import wraps
init_info = {'q': 'quit'}
usr_info = {}
story_info = None
usr = None


def num(func):
    init_info[str(len(init_info))] = func

    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


def auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global usr
        usr = input('请输入用户名: ')
        if usr in usr_info:
            pwd = input('请输入密码: ')
            if pwd == usr_info[usr]['pwd']:
                print('登陆成功')
                return func(*args, **kwargs)
            else:
                print('密码错误，登陆失败')
        else:
            print('用户名不存在，登陆失败')

    return wrapper


def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res:
            with open('access.log', 'at', encoding='utf-8') as f:
                f.write(f'{time.asctime()} {usr} {"充值" if func.__name__ == "register" else "消费"} {res}\n')
        return res
    return wrapper


@num
def register():
    usr = input('请输入用户名:')
    if usr in usr_info:
        print('该用户名存在， 请更换一个')
    else:
        pwd = input('该用户名合法，请输入密码: ')
        usr_info[usr] = {'pwd': pwd, 'balance': 0}
        update()
        print('注册成功')


@num
@log
@auth
def recharge():
    amount = int(input('请输入充值金额:'))
    usr_info[usr]['balance'] += amount
    update()
    print('充值成功，当前余额为: %d' % usr_info[usr]['balance'])
    return amount


def update():
    with open('.db.txt', 'wt', encoding='utf-8') as f:
        for k, v in usr_info.items():
            f.write(f"{k}:{v['pwd']}:{v['balance']}\n")
    os.remove('db.txt')
    os.rename('.db.txt', 'db.txt')


def load():
    with open('db.txt', 'rt', encoding='utf-8') as f:
        for line in f:
            usr, pwd, balance = line.split(':')
            usr_info[usr] = {'pwd': pwd, 'balance': int(balance)}
    with open('story_class.txt', 'rt', encoding='utf-8') as f:
        global story_info
        story_info = eval(f.read())
        print(story_info)


@num
@log
@auth
def story_read():
    print("0 玄幻武侠\n1 都市爱情 \n2 高效养猪36技")
    story = input('登陆成功，请选择小说类型: ')
    for k, v in story_info[story].items():
        print(f'编号:{k} 小说名称:{v[0]} 小说价格:{v[1]}')
    order = input('请输入小说编号:')
    y_or_n = input('金额为，请问是否确定扣费，确定输入y: ')
    if y_or_n == 'y':
        if usr_info[usr]['balance'] >= story_info[story][order][1]:
            usr_info[usr]['balance'] -= story_info[story][order][1]
            update()
            print('购买成功，请观看')
            with open(story_info[story][order][0], 'rt', encoding='utf-8') as f:
                for line in f:
                    print(line)
            return story_info[story][order][1]
        else:
            print('余额不足，请充值再进行购买！')
            return 0


def show_info(info_dict: dict):
    for k, v in info_dict.items():
        print(f'{k}: {v.__name__ if k != "q" else v}')


if __name__ == '__main__':
    load()
    while True:
        show_info(init_info)
        order = input('请输入指令：')
        if order == 'q':
            break
        else:
            init_info[order]()

