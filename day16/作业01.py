def out(x):

    def counter():
        nonlocal x
        x += 1
        return x
    return counter


counter = out(0)
print(counter())
print(counter())
print(counter())
print(counter())
print(counter())