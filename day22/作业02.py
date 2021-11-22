import random
import sys
import time


def print_rate(percent):
    num = int(percent / 100 * 50)
    print('\r[%-50s]%d%%' % ('#' * num, percent), end='')


for i in range(0, 100, 2):
    time.sleep(0.1)
    print_rate(i)


def random_val(num):
    val = []
    for _ in range(num):
        up = random.randint(65, 90)
        low = random.randint(97, 122)
        number = random.randint(0, 9)
        val.append(random.choice([chr(up), chr(low), str(number)]))
    return ''.join(val)


def copy_file(src, dst):
    with open(src, 'rt', encoding='utf-8') as f1, \
            open(dst, 'wt', encoding='utf-7') as f2:
        for line in f1:
            f2.write(line)


print(random_val(6))
for i in range(0, 100, 2):
    time.sleep(0.1)
    print_rate(i)
copy_file(sys.argv[1], sys.argv[2])