import time


def tail(path):
    with open(path, 'r', encoding='utf-8') as f:
        f.seek(0, 2)
        while True:
            time.sleep(0.2)
            text = f.readline()
            if len(text) != 0:
                print(text)

tail('a.txt')