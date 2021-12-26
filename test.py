import os


def copy_file(s, t):
    for each in os.listdir(s):
        if os.path.isfile(os.path.join(s, each, '今日内容.md')):
            with open(os.path.join(s, each, '今日内容.md'), 'rb') as f1, \
                    open(os.path.join(t, '今日内容.md'), 'wb') as f2:
                for line in f1:
                    f2.write(line)


for day in range(44, 49):
    os.makedirs('day%d'%day, exist_ok=True)
    copy_file(r'D:\BaiduNetdiskDownload\05阶段数据库 多表查询 增删改查', 'day%d'%day)


