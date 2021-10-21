import time


def tail(path):
    with open(path, 'a+', encoding='utf-8') as f:
        while True:
            time.sleep(0.3)
            text = f.readline()
            if len(text) != 0:
                print(text)


tail('access.log')