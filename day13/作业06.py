

def recharge():
    amount = input('amount=====>')
    amount = int(amount)
    with open('db.txt', 'a+', encoding='utf-8') as f:
        for line in f:
            if line.split()[0] == usr:
                balance = int(balance)



def withdraw():
    ...


def query():
    print('the balance is %s'%balance)


def transfer():
    target = input('usr====>')
    amount = input('amount==>')
    amount = int(amount)


order = {0:'quit', 1:recharge, 2:withdraw, 3:transfer, 4:query}

def login():
    usr_ipt = input('username===>').strip()
    pwd_ipt = input('password===>').strip()
    with open('db.txt', 'r', encoding='utf-8') as f:
        for line in f:
            global usr, balance, pwd
            usr, balance, pwd = line.split()
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
                    if order_of_usr == 0:
                        break
                    else:
                        order[k]()
                break
        else:
            print('账号或密码错误')


if __name__ =='__main__':
    usr, balance, pwd = None, None, None
    login()
