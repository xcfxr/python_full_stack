import time
time.sleep(10)
for i in range(3):
    usr = input('请输入账号:')
    pwd = input('请输入密码:')
    if usr == 'xuce' and pwd == '123':
        print('登录成功')
        break
    else:
        print('密码错误，一共{}次机会，还剩{}次'.format(3, 2-i))
else:
    print('次数用尽， 等待5min')
    time.sleep(300)