from multiprocessing import Queue, JoinableQueue, Process
from multiprocessing import current_process


def producer(food, q):
    q.put(food)
    print("生产者%s生产了%s" % (current_process().name, food))


def consumer(q):
    while True:
        food = q.get()
        print("消费者%s消费了%s" % (current_process().name, food))
        q.task_done()


if __name__ == '__main__':
    #q = Queue(5)
    q = JoinableQueue(5)
    p1 = Process(target=producer, name='p1', args=('包子', q))
    p2 = Process(target=producer, name='p2', args=('奶茶', q))
    c1 = Process(target=consumer, name='c1', args=(q,), daemon=True)
    c2 = Process(target=consumer, name='c2', args=(q,), daemon=True)
    p1.start()
    p2.start()
    c1.start()
    c2.start()
    p1.join()
    p2.join()
    q.join()
