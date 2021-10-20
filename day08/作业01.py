for i in range(1, 10):
    for j in range(1, i+1):
        res = '%d * %d = %d'%(j, i, j * i)
        print('{:<10}'.format(res), end=' ')
    print('')