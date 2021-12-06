# 1. 在元类中控制把自定义类的数据属性都变成大写
class Mymeta(type):
    def __new__(mcs, cls_name, cls_base, cls_dict):
        new_cls_dict = {}
        for k, v in cls_dict.items():
            if not callable(cls_dict[k]) and not k.startswith('__'):
                new_cls_dict[k.upper()] = v
            else:
                new_cls_dict[k] = v
        return super().__new__(mcs, cls_name, cls_base, new_cls_dict)

    def __call__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.__init__(obj, *args, **kwargs)
        return obj


class Foo(metaclass=Mymeta):
    sex = 'male'

    def __init__(self, name, age):
        self.name = name
        self.age = age


print(Foo.__dict__)
print(Foo("xucee", 18).SEX)

