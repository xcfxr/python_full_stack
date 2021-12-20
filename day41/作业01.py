from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

pool1 = ThreadPoolExecutor()
pool2 = ProcessPoolExecutor()


def func1():
    ...


def func2():
    ...


pool1.submit(func1).add_done_callback(func2)


from gevent import monkey; monkey.patch_all()
from gevent import spawn
