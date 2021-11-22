z = 7  # 定义全局变量


def foo(arg):
    x = 1
    print(locals())
    print('x=', x)
    locals()['x'] = 2  # 修改的是局部名字空间的拷贝，而实际的局部名字空间中的变量值并无影响。
    print(locals())
    print("x=", x)


foo(3)
print(globals())
print('z=', z)
globals()["z"] = 8  # globals（）返回的是实际的全局名字空间，修改变量z的值
print(globals())
print("z=", z)
print(locals())