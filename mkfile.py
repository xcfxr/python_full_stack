import os
mode = '作业'
path = r'D:\python全栈\day{}\{}{:0>2}.py'
num = 4
day = 12
for i in range(1, num+1):
    with open(path.format(day, mode, i), 'w', encoding='utf-8'):
        ...