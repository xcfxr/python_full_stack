import json
import time
usr_info = None


def load():
    with open('usr.json', 'rt', encoding='utf-8') as f:
        global usr_info
        usr_info = json.load(f)


def register():
    name = input('请输入用户名---->')
    pwd = input('请输入密码---->')
    usr = {'name': name, 'pwd': pwd, 'time': time.asctime()}
    usr_info.append(usr)
    with open('usr.json', 'wt', encoding='utf-8') as f:
        json.dump(usr_info, f)
