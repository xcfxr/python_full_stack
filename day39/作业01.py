from multiprocessing import Process, current_process
'''
进程对象：Process类产生的对象，具有一些方法
'''
print(current_process().pid)
p = Process()
p.terminate()
p.is_alive()


'''
僵尸进程：一个子进程结束后不会立马销毁，等待父进程清理
孤儿进程：一个子进程运行过程中，父进程暴毙了，交给操作系统管理
守护进程：父进程一死，其守护进程也跟着死
互斥锁：同一时间只有一个进程能够访问
队列：get、put、full、empty方法，get方法会阻塞， 等于管道+锁
IPC机制：利用队列进行进程间的通信
'''