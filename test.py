import os


def copy_file(s, t):
    for each in os.listdir(s):
        if os.path.isfile(os.path.join(s, each)):
            with open(os.path.join(s, each), 'rb') as f1, \
                    open(os.path.join(t, each), 'wb') as f2:
                for line in f1:
                    f2.write(line)
        else:
            os.makedirs(os.path.join(t, each), exist_ok=True)
            copy_file(os.path.join(s, each), os.path.join(t, each))

for day in range(20, 30):
    os.makedirs('day%d'%day, exist_ok=True)
    copy_file('D:/BaiduNetdiskDownload/02阶段Python面向对象编程/day%d/代码'%day, 'day%d'%day)


