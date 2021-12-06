'''
2、在元类中控制自定义的类无需__init__方法

1.元类帮其完成创建对象，以及初始化操作；

2.要求实例化时传参必须为关键字形式，否则抛出异常TypeError: must use keyword argument

3.key作为用户自定义类产生对象的属性，且所有属性变成大写
'''
class Mymeta(type):

    def __call__(cls, *args, **kwargs):
        if len(args) > 0:
            raise TypeError('must use keyword argument')
        obj = object.__new__(cls)
        for k, v in kwargs.items():
            setattr(obj,  k.upper(), v)
        return obj


class Foo(metaclass=Mymeta):
    sex = 'male'



print(Foo.__dict__)
foo = Foo(name = "xucee", age = 18)
print(foo.__dict__)