def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(10):
    print(fibonacci(i), end=' ')
print()


def list_print(l):
    for each in l:
        if type(each) == list:
            list_print(each)
        else:
            print(each, end=' ')


l = [1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15]]]]]]]
list_print(l)
