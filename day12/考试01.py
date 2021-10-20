usr_in = input('请输入用户名：')
pwd_in = input('请输入密码：')
with open('user.txt', 'at', encoding='utf-8') as f:
    f.write(usr_in)
    f.write(':')
    f.write(pwd_in)
    f.write('\n')
