import os
while True:
    source = input('输入源路径')
    dst = input('输入目标路径')
    if os.path.exists(source):
        print('源文件不存在')
        continue
    with open(source, 'rt', encoding='utf-8') as f1, \
        open(dst, 'wt', encoding='utf-8') as f2:
        for line in f1:
            f2.write(line)