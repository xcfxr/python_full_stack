from functools import wraps


def auth(db_type):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return wrapper
    return deco


@auth('file')
def index():
    print('hello')
