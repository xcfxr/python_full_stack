def deco1(func):
    print('this is load deco1')

    def wrapper(*args, **kwargs):
        print('this is run deco1')
        return func(*args, **kwargs)
    return wrapper


def deco2(func):
    print('this is load deco2')

    def wrapper(*args, **kwargs):
        print('this is run deco2')
        return func(*args, **kwargs)
    return wrapper


def deco3(func):
    print('this is load deco3')

    def wrapper(*args, **kwargs):
        print('this is run deco3')
        return func(*args, **kwargs)
    return wrapper


@deco1 # index=deco1(deco2.wrapper的内存地址)
@deco2 # deco2.wrapper的内存地址=deco2(deco3.wrapper的内存地址)
@deco3 # deco3.wrapper的内存地址=deco3(index)
def index():
    pass

index()