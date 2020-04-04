import threading
from time import sleep, ctime


loops = [4, 2]

def loop(nloop, nsec):
    print("start loop", nloop, "at:", ctime())
    sleep(nsec)
    print("loop", nloop, "done at:", ctime())


class ThreadFunc():
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.res = self.func(*self.args)


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    
    def get_result(self):
        return self.res

    def run(self):
        self.res = self.func(*self.args)





def test_main_thread_func():
    print("starting at:", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        t.setName("threads-%d" % i)
        threads.append(t)

    for i in nloops:
        print("start thread: %s" % threads[i].getName())
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("all done at:", ctime())


def test_main_thread_obj():
    print("starting at:", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        t.setName("threads-%d" % i)
        threads.append(t)

    for i in nloops:
        print("start thread: %s" % threads[i].getName())
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("all done at:", ctime())


def test_main_thread_subobj():
    print("starting at:", ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        t.setName("threads-%d" % i)
        threads.append(t)

    for i in nloops:
        print("start thread: %s" % threads[i].getName())
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print("all done at:", ctime())


