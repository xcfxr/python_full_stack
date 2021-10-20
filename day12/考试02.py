usr_in = input('请输入用户名：')
pwd_in = input('请输入密码：')
with open('user.txt', 'rt', encoding='utf-8') as f:
    for line in f:
        usr, pwd = line.strip().split(':')
        if usr == usr_in and pwd == pwd_in:
            print('login in successfully')
            break
    else:
        print('账号or密码错误')