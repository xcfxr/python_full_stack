username = 'xuce'
password = '123'
for i in range(3):
    inp_name = input('请输入您的账号：')
    inp_pwd = input('请输入您的密码：')

    if inp_name == username and inp_pwd == password:
        print('登录成功')
        while True:
            cmd = input("输入命令>: ")
            if cmd == 'q':  # 整个程序结束，退出所有while循环
                break
            else:
                print('命令{x}正在运行'.format(x=cmd))
        break
    else:
        print('账号名或密码错误')
else:
    print('输错3次，退出')