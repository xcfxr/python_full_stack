import os


def to_order(usr, order_of_usr):
    global f1, f2
    with open('db.txt', 'r', encoding='utf-8') as f1, \
            open('.db.txt', 'w', encoding='utf-8') as f2:
        order[order_of_usr]()



def recharge():
    for line in f1:
        if line.split()[0] == usr:
            amount = input('amount=====>')
            amount = int(amount)
            _, balance, pwd = line.split()
            balance = int(balance)
            balance += amount
            line = ' '.join([usr, str(balance), pwd])
            line += '\n'
        f2.write(line)


def withdraw():
    for line in f1:
        if line.split()[0] == usr:
            amount = input('amount=====>')
            amount = int(amount)
            _, balance, pwd = line.split()
            balance = int(balance)
            balance -= amount
            line = ' '.join([usr, str(balance), pwd])
            line += '\n'
        f2.write(line)


def query():
    for line in f1:
        if line.split()[0] == usr:
            _, balance, pwd = line.split()
            print('the balance is %s' % balance)
            break


def transfer():
    target = input('usr====>')
    amount = input('amount==>')
    amount = int(amount)
    for line in f1:
        q_usr, balance, pwd = line.split()
        if q_usr == target:
            balance = int(balance) + amount
        elif q_usr == usr:
            balance = int(balance) - amount
        line = ' '.join([usr, str(balance), pwd])
        f2.write(line)
        f2.write('\n')


order = {'0': 'quit', '1': recharge, '2': withdraw, '3': transfer, '4': query}


def login():
    usr_ipt = input('username===>').strip()
    pwd_ipt = input('password===>').strip()
    with open('db.txt', 'r', encoding='utf-8') as f:
        for line in f:
            global usr
            usr, _, pwd = line.split()
            if usr == usr_ipt and pwd == pwd_ipt:
                print('log in successfully')
                while True:
                    print('please input the order：')
                    for k, v in order.items():
                        if type(v) != str:
                            print(k, v.__name__, end=' ')
                        else:
                            print(k, v, end=' ')
                    order_of_usr = input()
                    if not order_of_usr.isdigit():
                        print('the order must be number 1 to 3')
                        continue
                    if order_of_usr == '0':
                        break
                    else:
                        to_order(usr, order_of_usr)
                break
        else:
            print('账号或密码错误')
    os.remove('db.txt')
    os.rename('.db.txt', 'db.txt')


if __name__ == '__main__':
    usr = None
    login()
