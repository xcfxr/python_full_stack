import time

usr_info = {}


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func()
        end = time.time()
        print(f'当前被装饰对象[{func.__name__}] 执行时间为: [{end - start}]')
        return res
    return wrapper


def auth(func):
    def wrapper(*args, **kwargs):
        usr = input("请输入账号========>")
        if usr in usr_info:
            now = time.time()
            struct_time = time.strptime(usr_info[usr]['time'], "%Y-%m-%d %H:%M:%S")
            last = time.mktime(struct_time)
            if now - last <= 600:
                print('hello')
                now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
                usr_info[usr]['time'] = now
                update()
                return func(*args, **kwargs)
            pwd = input("请输入密码========>")
            if pwd == usr_info[usr]['password']:
                print('hello')
                now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(now))
                usr_info[usr]['time'] = now
                update()
                return func(*args, **kwargs)
            else:
                print('密码错误')
        else:
            print('账号不存在')
    return wrapper


@auth
@timer
def index():
    time.sleep(1.5)
    return "hello"


def update():
    with open('usr_and_pwd.txt', 'wt', encoding='utf-8') as f:
        f.write(str(usr_info))



if __name__ == "__main__":
    with open('usr_and_pwd.txt', 'rt', encoding='utf-8') as f:
        info = f.read()
        usr_info = eval(info)
    index()
