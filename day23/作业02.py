import hashlib
import sys

filename = sys.argv[1]
with open(filename, 'rt', encoding='utf-8') as f:
    f.seek(1000, 0)
    m = hashlib.sha1()
    m.update(f.read(500))
    print(m.hexdigest())