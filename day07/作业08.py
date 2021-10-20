count = 0
while count<3:
    usr = input('请输入账号:')
    pwd = input('请输入密码:')
    if usr == 'xuce' and pwd == '123':
        print('登录成功')
        break
    else:
        print('密码错误，一共{}次机会，还剩{}次'.format(3, 2-count))
    count += 1
    if count== 3:
        while True:
            again = input('次数用尽，是否继续，继续输入Y或y，推出输入N或n：')
            if again in "Nn":
                break
            elif again in "Yy":
                count = 0
                break
            else:
                print('请输入Y、y、N、n中的一个')
