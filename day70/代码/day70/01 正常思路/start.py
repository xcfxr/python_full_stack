from notify import *


def send_all(content):
    wechat(content)
    qq(content)
    email(content)

if __name__ == '__main__':
    send_all('啥时候放长假')