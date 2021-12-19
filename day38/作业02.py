import time
from multiprocessing import Process


def task(name):
    print("%s is running" % name)
    time.sleep(1)
    print("%s is sleeping" % name)


class Myprocess(Process):
    def run(self):
        super().run()


if __name__ == "__main__":
    p1 = Process(target=task, kwargs={"name": "p1"})
    p2 = Process(target=task, kwargs={"name": "p2"})
    p1.start()
    p2.start()
    p3 = Myprocess(target=task, kwargs={"name": "p3"})
    p4 = Myprocess(target=task, kwargs={"name": "p4"})
    p3.start()
    p4.start()
