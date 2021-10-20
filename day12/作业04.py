while True:
    msg = """
    0 退出
    1 登录
    2 注册
    """
    print(msg)
    cmd = input('请输入命令编号>>: ').strip()
    if not cmd.isdigit():
        print('必须输入命令编号的数字，傻叉')
        continue

    if cmd == '0':
        break
    elif cmd == '1':
        usr_in = input('请输入用户名：')
        pwd_in = input('请输入密码：')
        with open('user.txt', 'rt', encoding='utf-8') as f:
            for line in f:
                usr, pwd = line.strip().split(':')
                if usr == usr_in and pwd == pwd_in:
                    print('login in successfully')
                    break
            else:
                print('登陆失败')
    elif cmd == '2':
        usr_in = input('请输入用户名：')
        pwd_in = input('请输入密码：')
        with open('user.txt', 'at', encoding='utf-8') as f:
            f.write(usr_in)
            f.write(':')
            f.write(pwd_in)
            f.write('\n')

    else:
        print('输入的命令不存在')