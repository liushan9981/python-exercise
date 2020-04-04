from random import randint
from time import sleep
from queue import Queue
from .test_thread_func import MyThread



def write_q(queue):
    print("producing object for Q...",)
    queue.put('xxx', 1)
    print("size now", queue.qsize())

def read_q(queue):
    val = queue.get(1)
    print("consumed object from Q...size now", queue.qsize())

def writer(queue, loops):
    for i in range(loops):
        write_q(queue)
        sleep(randint(1, 3))

def reader(queue, loops):
    for i in range(loops):
        read_q(queue)
        sleep(randint(2, 5))

funcs = [writer, reader]
nfuncs = range(len(funcs))

def testqueue():
    nloops = randint(2, 5)
    q = Queue(32)

    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i], (q, nloops), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()

    print("done")

