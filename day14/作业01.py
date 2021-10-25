import os


def modify(filename, source, target):
    with open(filename, 'r', encoding='utf-8') as f1, \
            open('temporary.txt', 'w', encoding='utf-8') as f2:
        for line in f1:
            f2.write(line.replace(source, target))
    os.remove(filename)
    os.rename('temporary.txt', filename)
