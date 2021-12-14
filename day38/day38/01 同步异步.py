import time
'https://www.cnblogs.com/Dominic-Ji/articles/10929381.html'

def func():
    time.sleep(3)
    print('hello world')


if __name__ == '__main__':
    res = func()  # 同步调用
    print('hahaha')