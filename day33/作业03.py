'3、在元类中控制自定义的类产生的对象相关的属性全部为隐藏属性'
class Mymeta(type):

    def __call__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        cls.__init__(obj, *args, **kwargs)
        new_dict = {}
        for k, v in obj.__dict__.items():
            if not k.startswith("__"):
                new_dict["_%s__%s"%(cls.__name__, k)] = v
            else:
                new_dict[k] = v
        obj.__dict__ = new_dict
        return obj


class Foo(metaclass=Mymeta):
    sex = 'male'
    def __init__(self, name, age):
        self.name = name
        self.age = age

print(Foo("xucee", 18).__dict__)