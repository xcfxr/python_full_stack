import hashlib


def login():
    pwd = input('请输入密码======>')
    m = hashlib.md5()
    m.update(pwd.encode('utf-8'))
    res = m.hexdigest()
    print(res)

login()