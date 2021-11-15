def iter_take(obj):
    obj = iter(obj)
    while True:
        try:
            yield next(obj)
        except StopIteration as e:
            break


for each in iter_take('abc'):
    print(each)