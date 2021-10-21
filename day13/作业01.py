import os


def copy(path, source, target):
    with open(path, encoding='utf-8') as f1, open('temporary.txt', 'w', encoding='utf-8') as f2:
        for line in f1:
            f2.write(line.replace(source, target))
    os.remove(path)
    os.rename('temporary.txt', path)

