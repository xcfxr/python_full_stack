from functools import wraps
import time


def log(filename):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            with open(filename, 'at', encoding='utf-8') as f:
                info = ' '.join([time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())), func.__name__,'run'])
                f.write(info)
            return func(**kwargs)
        return wrapper
    return deco


@log('access.log')
def f1():
    print('hello')


if __name__ == '__main__':
    f1()