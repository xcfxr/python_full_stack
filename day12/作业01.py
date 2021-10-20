source = input('输入源路径')
dst = input('输入目标路径')
with open(source, 'rb') as f1, \
    open(dst, 'wb') as f2:
    for line in f1:
        f2.write(line)