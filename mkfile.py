import os
mode = '作业'
path = r'D:\python_full_stack\day{}\{}{:0>2}.py'
num = 4
day = 23
for i in range(1, num+1):
    with open(path.format(day, mode, i), 'w', encoding='utf-8'):
        ...