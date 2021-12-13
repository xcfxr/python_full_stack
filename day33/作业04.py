'4、基于元类实现单例模式'

# 通过模块导入实现
import cls_singleton

p1 = cls_singleton.singleton
p2 = cls_singleton.singleton
p3 = cls_singleton.singleton
print(p1 is p2 is p3)


# 通过装饰器实现
def wrapper(cls):
    def inner(*args, **kwargs):
        if cls._singleton is None:
            cls._singleton = cls(*args, **kwargs)
            return cls._singleton
        else:
            return cls._singleton

    return inner


@wrapper
class Foo:
    _singleton = None


p1 = Foo()
p2 = Foo()
p3 = Foo()
print(p1 is p2 is p3)


# 通过__new__实现
class Foo:
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if Foo._singleton is None:
            Foo._singleton = super().__new__(cls, *args, **kwargs)
        return Foo._singleton


p1 = Foo()
p2 = Foo()
p3 = Foo()
print(p1 is p2 is p3)


# 通过classmethod实现
class Foo:
    _singleton = None

    @classmethod
    def cls_singleton(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = Foo(*args, **kwargs)
        return cls._singleton


p1 = Foo.cls_singleton()
p2 = Foo.cls_singleton()
p3 = Foo.cls_singleton()
print(p1 is p2 is p3)


# 通过元类实现
class Mymeta(type):
    def __call__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = type.__call__(cls, *args, **kwargs)
        return cls._singleton


class Foo(metaclass=Mymeta):
    _singleton = None


p1 = Foo()
p2 = Foo()
p3 = Foo()
print(p1 is p2 is p3)


## 元类实现
class Mymeta(type):
    def __call__(cls, *args, **kwargs):
        if cls._singleton is None:
            cls._singleton = type.__call__(cls, *args, **kwargs)
        return cls._singleton


class Foo(metaclass=Mymeta):
    _singleton = None


p1 = Foo()
p2 = Foo()
p3 = Foo()
print(p1 is p2 is p3)